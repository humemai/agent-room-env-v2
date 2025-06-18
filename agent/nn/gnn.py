"""A lot copied from https://github.com/migalkin/StarE"""

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

from .attention import AttentionAggregator
from .mlp import MLP
from .stare_conv import StarEConvLayer
from .transformer import TransformerMemoryNet
from .utils import process_graph


class GNN(torch.nn.Module):
    """Graph Neural Network model. This model is used to compute the Q-values for the
    memory management (remember and forget) policies. This model has N layers of GCNConv
    or StarEConv layers and two MLPs for the two memory management polices,
    respectively.

    Now supports both GNN-based and Transformer-based architectures.
    """

    def __init__(
        self,
        entities: list[str],
        relations: list[str],
        gcn_layer_params: dict = {
            "type": "StarE",
            "embedding_dim": 8,
            "num_layers": 2,
            "gcn_drop": 0.1,
            "triple_qual_weight": 0.8,
        },
        relu_between_gcn_layers: bool = True,
        dropout_between_gcn_layers: bool = True,
        mlp_params: dict = {"num_hidden_layers": 2, "dueling_dqn": True},
        rotational_for_relation: bool = True,
        device: str = "cpu",
        forget_needs_rl: bool = True,
        remember_needs_rl: bool = True,
        separate_network_type: str = None,
        architecture_type: str = "gnn",  # New parameter: "gnn" or "transformer"
        transformer_params: dict = {  # New parameter for transformer config
            "num_layers": 2,
            "num_heads": 8,
            "dropout": 0.1,
        },
    ) -> None:
        """Initialize the GNN/Transformer model.

        Args:
            entities: List of entities
            relations: List of relations
            gcn_layer_params: The parameters for the GCN layers
            relu_between_gcn_layers: Whether to apply ReLU activation between GCN layers
            dropout_between_gcn_layers: Whether to apply dropout between GCN layers
            mlp_params: The parameters for the MLPs
            rotational_for_relation: Whether to use rotational embeddings for relations
            device: The device to use. Default is "cpu".
            forget_needs_rl: Whether forget policy needs RL components
            remember_needs_rl: Whether remember policy needs RL components
            separate_network_type: Type of separate network ("forget", "remember", or None for shared)
            architecture_type: Type of architecture to use ("gnn" or "transformer")
            transformer_params: Parameters for transformer architecture

        """
        super(GNN, self).__init__()
        self.entities = entities
        self.relations = relations
        self.gcn_layer_params = gcn_layer_params
        self.gcn_type = gcn_layer_params["type"].lower()
        self.mlp_params = mlp_params
        self.rotational_for_relation = rotational_for_relation
        self.device = device
        self.embedding_dim = gcn_layer_params["embedding_dim"]
        self.forget_needs_rl = forget_needs_rl
        self.remember_needs_rl = remember_needs_rl
        self.separate_network_type = separate_network_type
        self.architecture_type = architecture_type.lower()
        self.transformer_params = transformer_params

        # If using transformer architecture, create transformer model and return
        if self.architecture_type == "transformer":
            self.transformer_model = TransformerMemoryNet(
                entities=entities,
                relations=relations,
                embedding_dim=self.embedding_dim,
                num_transformer_layers=transformer_params["num_layers"],
                num_heads=transformer_params["num_heads"],
                dropout=transformer_params["dropout"],
                mlp_params=mlp_params,
                device=device,
                forget_needs_rl=forget_needs_rl,
                remember_needs_rl=remember_needs_rl,
                separate_network_type=separate_network_type,
            )
            # Move to device
            self.to(self.device)
            return

        # Continue with GNN initialization for non-transformer architectures
        self.entity_to_idx = {entity: idx for idx, entity in enumerate(self.entities)}
        self.relation_to_idx = {
            relation: idx for idx, relation in enumerate(self.relations)
        }

        self.entity_embeddings = torch.nn.Parameter(
            torch.Tensor(len(self.entities), self.embedding_dim)
        ).to(self.device)
        torch.nn.init.xavier_normal_(self.entity_embeddings)

        if self.rotational_for_relation:
            # init relation embeddings with phase values
            phases = (
                2 * np.pi * torch.rand(len(self.relations), self.embedding_dim // 2)
            )
            self.relation_embeddings = torch.nn.Parameter(
                torch.cat(
                    [
                        torch.cat([torch.cos(phases), torch.sin(phases)], dim=-1),
                        torch.cat([torch.cos(phases), -torch.sin(phases)], dim=-1),
                    ],
                    dim=0,
                )
            )
        else:
            self.relation_embeddings = torch.nn.Parameter(
                torch.Tensor(len(self.relations), self.embedding_dim)
            ).to(self.device)
            torch.nn.init.xavier_normal_(self.relation_embeddings)

        self.relu_between_gcn_layers = relu_between_gcn_layers
        self.dropout_between_gcn_layers = dropout_between_gcn_layers
        self.relu = torch.nn.ReLU()
        self.drop = torch.nn.Dropout(self.gcn_layer_params["gcn_drop"])

        if self.gcn_type.lower() == "stare":
            self.gcn_layers = torch.nn.ModuleList(
                [
                    StarEConvLayer(
                        in_channels=self.embedding_dim,
                        out_channels=self.embedding_dim,
                        num_rels=len(relations),
                        gcn_drop=self.gcn_layer_params["gcn_drop"],
                        triple_qual_weight=self.gcn_layer_params["triple_qual_weight"],
                        device=device,
                    )
                    for _ in range(self.gcn_layer_params["num_layers"])
                ]
            ).to(self.device)

        elif self.gcn_type.lower() == "vanilla" or self.gcn_type.lower() == "gcn":
            self.gcn_layers = torch.nn.ModuleList(
                [
                    GCNConv(
                        self.embedding_dim,
                        self.embedding_dim,
                        improved=False,
                        add_self_loops=False,
                        normalize=False,
                    )
                    for _ in range(self.gcn_layer_params["num_layers"])
                ]
            ).to(self.device)

            for layer in self.gcn_layers:
                if isinstance(layer, torch.nn.Linear):
                    torch.nn.init.xavier_normal_(layer.weight)
                    if layer.bias is not None:
                        layer.bias.data.zero_()

        else:
            raise ValueError(f"{self.gcn_type} is not a valid GNN type.")

        # Conditionally create policy-specific components
        if separate_network_type == "forget":
            # Only create forget-related components
            self.attention_aggregator_forget = AttentionAggregator(
                embedding_dim=self.embedding_dim,
                device=device,
            )
            self.mlp_forget = MLP(
                n_actions=3,  # lru, lfu, fifo
                input_size=self.embedding_dim,  # aggregated embedding
                hidden_size=self.embedding_dim,
                device=device,
                **mlp_params,
            )
        elif separate_network_type == "remember":
            # Only create remember-related components
            self.mlp_remember = MLP(
                n_actions=2,  # remember, forget
                input_size=self.embedding_dim * 3,
                hidden_size=self.embedding_dim,
                device=device,
                **mlp_params,
            )
        else:
            # Shared network: conditionally create components based on needs
            if forget_needs_rl:
                self.attention_aggregator_forget = AttentionAggregator(
                    embedding_dim=self.embedding_dim,
                    device=device,
                )
                self.mlp_forget = MLP(
                    n_actions=3,  # lru, lfu, fifo
                    input_size=self.embedding_dim,  # aggregated embedding
                    hidden_size=self.embedding_dim,
                    device=device,
                    **mlp_params,
                )

            if remember_needs_rl:
                self.mlp_remember = MLP(
                    n_actions=2,  # remember, forget
                    input_size=self.embedding_dim * 3,
                    hidden_size=self.embedding_dim,
                    device=device,
                    **mlp_params,
                )

        # Move the entire model to the specified device
        self.to(self.device)

    def process_batch(self, data: np.ndarray) -> tuple[
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
        torch.Tensor,
    ]:
        r"""Process the data batch.

        Args:
            data: The input data as a batch. This is the same as what the `forward`
                method receives. We will make them in to a batched version of the
                entity embeddings, relation embeddings, edge index, edge type, and
                qualifiers. StarE needs all of them, while vanilla-GCN only needs the
                entity embeddings and edge index.

        Returns:
            edge_idx: The shape is [2, num_quadruples]
            edge_type: The shape is [num_quadruples]
            quals: The shape is [3, number of qualifier key-value pairs]

            edge_idx_inv: The shape is [2, num_quadruples]
            edge_type_inv: The shape is [num_quadruples]
            quals_inv: The shape is [3, number of qualifier key-value pairs]

            short_memory_idx: The shape is [number of short-term memories]
                the idx indexes `edge_idx` and `edge_type`

            num_short_memories: The number of short-term memories in each sample

            num_entities_per_sample: The number of entities in each sample

        """
        entity_embeddings_batch = []
        relation_embeddings_batch = []
        edge_idx_batch = []
        edge_type_batch = []
        quals_batch = []

        entity_embeddings_batch_inv = []
        relation_embeddings_batch_inv = []
        edge_idx_inv_batch = []
        edge_type_inv_batch = []
        quals_inv_batch = []

        short_memory_idx_batch = []

        entity_offset_batch = [0]
        relation_offset_batch = [0]
        edge_offset_batch = [0]

        num_entities_per_sample = []

        for idx, sample in enumerate(data):
            (
                entities,
                relations,
                edge_idx,
                edge_type,
                quals,
                edge_idx_inv,
                edge_type_inv,
                quals_inv,
                short_memory_idx,
            ) = process_graph(sample, device=self.device)

            num_entities_per_sample.append(len(entities))

            for entity in entities:
                entity_embeddings_batch.append(
                    self.entity_embeddings[self.entity_to_idx[entity]]
                )
            for relation in relations:
                relation_embeddings_batch.append(
                    self.relation_embeddings[self.relation_to_idx[relation]]
                )
            edge_idx_batch.append(edge_idx)
            edge_type_batch.append(edge_type)
            quals_batch.append(quals)

            for entity in entities:
                entity_embeddings_batch_inv.append(
                    self.entity_embeddings[self.entity_to_idx[entity]]
                )
            for relation in relations:
                relation_embeddings_batch_inv.append(
                    self.relation_embeddings[self.relation_to_idx[relation]]
                )
            edge_idx_inv_batch.append(edge_idx_inv)
            edge_type_inv_batch.append(edge_type_inv)
            quals_inv_batch.append(quals_inv)

            short_memory_idx_batch.append(short_memory_idx)

            if idx < len(data) - 1:
                entity_offset_batch.append(len(entities) + entity_offset_batch[-1])
                relation_offset_batch.append(len(relations) + relation_offset_batch[-1])
                edge_offset_batch.append(edge_idx.size(1) + edge_offset_batch[-1])

        entity_embeddings_batch = torch.stack(entity_embeddings_batch, dim=0)
        entity_embeddings_batch_inv = torch.stack(entity_embeddings_batch_inv, dim=0)
        entity_embeddings = torch.cat(
            [entity_embeddings_batch, entity_embeddings_batch_inv], dim=0
        )

        relation_embeddings_batch = torch.stack(relation_embeddings_batch, dim=0)
        relation_embeddings_batch_inv = torch.stack(
            relation_embeddings_batch_inv, dim=0
        )
        relation_embeddings = torch.cat(
            [relation_embeddings_batch, relation_embeddings_batch_inv], dim=0
        )

        edge_idx_batch = [a + b for a, b in zip(edge_idx_batch, entity_offset_batch)]
        edge_idx_batch = torch.cat(edge_idx_batch, dim=1).to(self.device)

        edge_idx_batch_inv = torch.cat(
            [
                a + b + entity_embeddings_batch.shape[0]
                for a, b in zip(edge_idx_inv_batch, entity_offset_batch)
            ],
            dim=1,
        ).to(self.device)
        edge_idx = torch.cat([edge_idx_batch, edge_idx_batch_inv], dim=1)

        edge_type_batch = [
            a + b for a, b in zip(edge_type_batch, relation_offset_batch)
        ]
        edge_type_batch = torch.cat(edge_type_batch, dim=0).to(self.device)

        edge_type_batch_inv = torch.cat(
            [
                a + b + relation_embeddings_batch.shape[0]
                for a, b in zip(edge_type_inv_batch, relation_offset_batch)
            ],
            dim=0,
        ).to(self.device)
        edge_type = torch.cat([edge_type_batch, edge_type_batch_inv], dim=0)

        quals_batch = torch.cat(
            [
                a + torch.tensor([c, b, d], device=self.device).reshape(-1, 1)
                for a, b, c, d in zip(
                    quals_batch,
                    entity_offset_batch,
                    relation_offset_batch,
                    edge_offset_batch,
                )
            ],
            dim=1,
        ).to(self.device)
        quals = quals_batch.repeat(1, 2)

        num_short_memories = torch.tensor(
            [len(short_memory_idx) for short_memory_idx in short_memory_idx_batch],
            device=self.device
        )
        short_memory_idx = torch.cat(
            [a + b for a, b in zip(short_memory_idx_batch, edge_offset_batch)], dim=0
        ).to(self.device)

        return (
            entity_embeddings,
            relation_embeddings,
            edge_idx,
            edge_type,
            quals,
            short_memory_idx,
            num_short_memories,
            torch.tensor(num_entities_per_sample, device=self.device),
        )

    def forward(self, data: np.ndarray, policy_type: str) -> list[torch.Tensor]:
        """Forward pass of the GNN/Transformer model.

        Args:
            data: The input data as a batch. Because of how it's processed, the data
                has to have a batch dimension, even if it's a single sample. The shape
                is [batch_size, num_quadruples, 4], where num_quadruples varies per
                sample.
            policy_type: The type of policy to compute Q-values for. Can be 'remember'
                or 'forget'.

        Returns:
            Q-values for different policies:
        """
        # If using transformer, delegate to transformer model
        if self.architecture_type == "transformer":
            return self.transformer_model(data, policy_type)
        
        # Continue with existing GNN forward pass
        # Validate policy type based on network configuration
        if self.separate_network_type == "forget" and policy_type != "forget":
            raise ValueError(f"This network is configured for forget policy only, got {policy_type}")
        if self.separate_network_type == "remember" and policy_type != "remember":
            raise ValueError(f"This network is configured for remember policy only, got {policy_type}")
        
        if policy_type == "remember" and not hasattr(self, 'mlp_remember'):
            raise ValueError("Remember policy components not available in this network")
        if policy_type == "forget" and not hasattr(self, 'mlp_forget'):
            raise ValueError("Forget policy components not available in this network")

        (
            entity_embeddings,
            relation_embeddings,
            edge_idx,
            edge_type,
            quals,
            short_memory_idx,
            num_short_memories,
            num_entities_per_sample,
        ) = self.process_batch(data)

        for layer_ in self.gcn_layers:
            if "stare" in self.gcn_type:
                entity_embeddings, relation_embeddings = layer_(
                    entity_embeddings=entity_embeddings,
                    relation_embeddings=relation_embeddings,
                    edge_idx=edge_idx,
                    edge_type=edge_type,
                    quals=quals,
                )
            elif "vanilla" in self.gcn_type:
                entity_embeddings = layer_(entity_embeddings, edge_idx)
            else:
                raise ValueError(f"{self.gcn_type} is not a valid GNN type.")

            if self.dropout_between_gcn_layers:
                entity_embeddings = self.drop(entity_embeddings)
            if self.relu_between_gcn_layers:
                entity_embeddings = F.relu(entity_embeddings)

        # Handle remember policy
        if policy_type == "remember":

            assert num_short_memories.sum() == short_memory_idx.size(0)
            triple = []
            for idx in short_memory_idx:
                triple_ = torch.cat(
                    [
                        entity_embeddings[edge_idx[0, idx]],
                        relation_embeddings[edge_type[idx]],
                        entity_embeddings[edge_idx[1, idx]],
                    ],
                    dim=0,
                )
                triple.append(triple_)

            triple = torch.stack(triple, dim=0)
            q_remember = self.mlp_remember(triple)

            q_remember_batch = [
                q_remember[start : start + num]
                for start, num in zip(
                    num_short_memories.cumsum(0).roll(1), num_short_memories
                )
            ]
            q_remember_batch[0] = q_remember[: num_short_memories[0]]

            return q_remember_batch

        # Handle forget policy with attention aggregation
        elif policy_type == "forget":
            # Get the first half of entity embeddings (original, not duplicated)
            entity_embeddings_first_half = entity_embeddings[
                : entity_embeddings.size(0) // 2
            ]

            # Create padded batch for efficient processing
            max_num_entities = max(num_entities_per_sample)
            batch_size = len(num_entities_per_sample)

            # Initialize padded tensor
            padded_embeddings = torch.zeros(
                batch_size, max_num_entities, self.embedding_dim, device=self.device
            )

            # Create attention mask
            attention_mask = torch.zeros(
                batch_size, max_num_entities, dtype=torch.bool, device=self.device
            )

            # Fill padded tensor and mask
            start_idx = 0
            for i, num_entities in enumerate(num_entities_per_sample):
                padded_embeddings[i, :num_entities] = entity_embeddings_first_half[
                    start_idx : start_idx + num_entities
                ]
                attention_mask[i, :num_entities] = True
                start_idx += num_entities

            # Single batched attention aggregation
            aggregated_embeddings = self.attention_aggregator_forget(
                padded_embeddings, attention_mask
            )  # (batch_size, embedding_dim)

            # Single batched MLP forward pass
            q_forget = self.mlp_forget(aggregated_embeddings)  # (batch_size, n_actions)

            # Convert back to list format for consistency
            q_forget_batch = [q_forget[i : i + 1] for i in range(batch_size)]

            return q_forget_batch

        else:
            raise ValueError(
                f"{policy_type} is not a valid policy type. Use 'remember' or 'forget'."
            )
