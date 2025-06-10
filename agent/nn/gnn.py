"""A lot copied from https://github.com/migalkin/StarE"""

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

from .attention import AttentionAggregator
from .mlp import MLP
from .stare_conv import StarEConvLayer
from .utils import process_graph


class GNN(torch.nn.Module):
    """Graph Neural Network model. This model is used to compute the Q-values for the
    memory management (remember and forget) policies. This model has N layers of GCNConv
    or StarEConv layers and two MLPs for the two memory management polices,
    respectively.

    Attributes:
        entities: List of entities
        relations: List of relations
        gcn_layer_params: The parameters for the GCN layers
        gcn_type: The type of GCN layer
        mlp_params: The parameters for the MLPs
        rotational_for_relation: Whether to use rotational embeddings for relations
        device: The device to use
        embedding_dim: The dimension of the embeddings
        entity_to_idx: The mapping from entities to indices
        relation_to_idx: The mapping from relations to indices
        entity_embeddings: The entity embeddings
        relation_embeddings: The relation embeddings
        relu_between_gcn_layers: Whether to apply ReLU activation between GCN layers
        dropout_between_gcn_layers: Whether to apply dropout between GCN layers
        relu: The ReLU activation function
        drop: The dropout layer
        gcn_layers: The GCN layers
        mlp_mm_forget: The MLP for forget
        mlp_mm_remember: The MLP for remember

    """

    def __init__(
        self,
        entities: list[str],
        relations: list[str],
        mm_forget_policy: str,
        mm_remember_policy: str,
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
    ) -> None:
        """Initialize the GNN model.

        Args:
            entities: List of entities
            relations: List of relations
            mm_forget_policy: memory management policy for forgetting long-term memory
            mm_remember_policy: memory management policy for remembering long-term memory
            gcn_layer_params: The parameters for the GCN layers
            relu_between_gcn_layers: Whether to apply ReLU activation between GCN layers
            dropout_between_gcn_layers: Whether to apply dropout between GCN layers
            mlp_params: The parameters for the MLPs
            rotational_for_relation: Whether to use rotational embeddings for relations
            device: The device to use. Default is "cpu".

        """
        super(GNN, self).__init__()
        self.entities = entities
        self.relations = relations
        self.mm_forget_policy = mm_forget_policy.lower()
        self.mm_remember_policy = mm_remember_policy.lower()
        self.gcn_layer_params = gcn_layer_params
        self.gcn_type = gcn_layer_params["type"].lower()
        self.mlp_params = mlp_params
        self.rotational_for_relation = rotational_for_relation
        self.device = device
        self.embedding_dim = gcn_layer_params["embedding_dim"]

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

        if self.mm_forget_policy == "rl":
            # Add attention aggregator for forget policy
            self.attention_aggregator = AttentionAggregator(
                embedding_dim=self.embedding_dim,
                device=device,
            )
            self.mlp_mm_forget = MLP(
                n_actions=3,  # lru, lfu, fifo
                input_size=self.embedding_dim,  # aggregated embedding
                hidden_size=self.embedding_dim,
                device=device,
                **mlp_params,
            )
        else:
            self.attention_aggregator = None
            self.mlp_mm_forget = None

        if self.mm_remember_policy == "rl":
            self.mlp_mm_remember = MLP(
                n_actions=2,  # remember, forget
                input_size=self.embedding_dim * 3,
                hidden_size=self.embedding_dim,
                device=device,
                **mlp_params,
            )
        else:
            self.mlp_mm_remember = None

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
            ) = process_graph(sample)

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
        edge_idx_batch = torch.cat(edge_idx_batch, dim=1)

        edge_idx_batch_inv = torch.cat(
            [
                a + b + entity_embeddings_batch.shape[0]
                for a, b in zip(edge_idx_inv_batch, entity_offset_batch)
            ],
            dim=1,
        )
        edge_idx = torch.cat([edge_idx_batch, edge_idx_batch_inv], dim=1)

        edge_type_batch = [
            a + b for a, b in zip(edge_type_batch, relation_offset_batch)
        ]
        edge_type_batch = torch.cat(edge_type_batch, dim=0)

        edge_type_batch_inv = torch.cat(
            [
                a + b + relation_embeddings_batch.shape[0]
                for a, b in zip(edge_type_inv_batch, relation_offset_batch)
            ],
            dim=0,
        )
        edge_type = torch.cat([edge_type_batch, edge_type_batch_inv], dim=0)

        quals_batch = torch.cat(
            [
                a + torch.tensor([c, b, d]).reshape(-1, 1)
                for a, b, c, d in zip(
                    quals_batch,
                    entity_offset_batch,
                    relation_offset_batch,
                    edge_offset_batch,
                )
            ],
            dim=1,
        )
        quals = quals_batch.repeat(1, 2)

        num_short_memories = torch.tensor(
            [len(short_memory_idx) for short_memory_idx in short_memory_idx_batch]
        )
        short_memory_idx = torch.cat(
            [a + b for a, b in zip(short_memory_idx_batch, edge_offset_batch)], dim=0
        )

        return (
            entity_embeddings,
            relation_embeddings,
            edge_idx,
            edge_type,
            quals,
            short_memory_idx,
            num_short_memories,
            torch.tensor(num_entities_per_sample),
        )

    def forward(self, data: np.ndarray) -> dict[str, list[torch.Tensor]]:
        """Forward pass of the GNN model.

        Args:
            data: The input data as a batch. Because of how it's processed, the data
            has to have a batch dimension, even if it's a single sample. The shape is
            [batch_size, num_quadruples, 4], where num_quadruples varies per sample.

        Returns:
            Dictionary with Q-values for different policies:
            - 'remember': Q-values for remember policy (if enabled)
            - 'forget': Q-values for forget policy (if enabled)
        """
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

        results = {}

        # Handle remember policy
        if self.mm_remember_policy == "rl":
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
            q_mm_remember = self.mlp_mm_remember(triple)

            q_mm_remember_batch = [
                q_mm_remember[start : start + num]
                for start, num in zip(
                    num_short_memories.cumsum(0).roll(1), num_short_memories
                )
            ]
            q_mm_remember_batch[0] = q_mm_remember[: num_short_memories[0]]
            results["remember"] = q_mm_remember_batch

        # Handle forget policy with attention aggregation
        if self.mm_forget_policy == "rl":
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
            aggregated_embeddings = self.attention_aggregator(
                padded_embeddings, attention_mask
            )  # (batch_size, embedding_dim)

            # Single batched MLP forward pass
            q_mm_forget = self.mlp_mm_forget(
                aggregated_embeddings
            )  # (batch_size, n_actions)

            # Convert back to list format for consistency
            q_mm_forget_batch = [q_mm_forget[i : i + 1] for i in range(batch_size)]
            results["forget"] = q_mm_forget_batch

        return results
