"""A lot copied from https://github.com/migalkin/StarE"""

from typing import Literal

import numpy as np
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

from .mlp import MLP
from .stare_conv import StarEConvLayer
from .utils import process_graph


class GNN(torch.nn.Module):
    """Graph Neural Network model. This model is used to compute the Q-values for the
    memory management and explore policies. This model has N layers of GCNConv or
    StarEConv layers and two MLPs for the memory management and explore policies,
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
        mlp_mm: The MLP for memory management policy
        mlp_explore: The MLP for explore policy

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
    ) -> None:
        """Initialize the GNN model.

        Args:
            entities: List of entities
            relations: List of relations
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
        # self.entity_embeddings.data[0] = 0  # NOT SURE ABOUT THIS

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
        # self.relation_embeddings.data[0] = 0  # NOT SURE ABOUT THIS

        self.relu_between_gcn_layers = relu_between_gcn_layers
        self.dropout_between_gcn_layers = dropout_between_gcn_layers
        self.relu = torch.nn.ReLU()
        self.drop = torch.nn.Dropout(self.gcn_layer_params["gcn_drop"])

        if "stare" in self.gcn_type:
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

        elif "vanilla" in self.gcn_type:
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

        self.mlp_mm = MLP(
            n_actions=3,
            input_size=self.embedding_dim * 3,  # [head, relation, tail]
            hidden_size=self.embedding_dim,
            device=device,
            **mlp_params,
        )
        self.mlp_explore = MLP(
            n_actions=5,
            input_size=self.embedding_dim,
            hidden_size=self.embedding_dim,
            device=device,
            **mlp_params,
        )

    def process_batch(self, data: np.ndarray) -> tuple[
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
            agent_entity_idx: The shape is [num batches]
                the idx indexes `entity_embeddings`

            num_short_memories: The number of short-term memories in each sample

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
        agent_entity_idx_batch = []

        entity_offset_batch = [0]
        relation_offset_batch = [0]
        edge_offset_batch = [0]

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
                agent_entity_idx,
            ) = process_graph(sample)

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
            agent_entity_idx_batch.append(agent_entity_idx)

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
        agent_entity_idx = torch.tensor(
            [a + b for a, b in zip(agent_entity_idx_batch, entity_offset_batch)]
        )

        return (
            entity_embeddings,
            relation_embeddings,
            edge_idx,
            edge_type,
            quals,
            short_memory_idx,
            num_short_memories,
            agent_entity_idx,
        )

    def forward(
        self, data: np.ndarray, policy_type: Literal["mm", "explore"]
    ) -> list[torch.Tensor]:
        """Forward pass of the GNN model.

        Args:
            data: The input data as a batch.
            policy_type: The policy type to use.

        Returns:
            The Q-values. The number of elements in the list is equal to the number of
            samples in the batch. Each element is a tensor of Q-values for the actions
            in the sample. The length of the tensor is equal to the number of actions
            in the sample.

        """
        (
            entity_embeddings,
            relation_embeddings,
            edge_idx,
            edge_type,
            quals,
            short_memory_idx,
            num_short_memories,
            agent_entity_idx,
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

        if policy_type == "mm":
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

            q_mm_ = self.mlp_mm(triple)

            q_mm = [
                q_mm_[start : start + num]
                for start, num in zip(
                    num_short_memories.cumsum(0).roll(1), num_short_memories
                )
            ]

            q_mm[0] = q_mm_[: num_short_memories[0]]

            return q_mm

        elif policy_type == "explore":
            node = []
            for idx in agent_entity_idx:
                node_ = entity_embeddings[idx]
                node.append(node_)

            node = torch.stack(node, dim=0)

            q_explore = self.mlp_explore(node)

            q_explore = [row.unsqueeze(0) for row in list(q_explore.unbind(dim=0))]

            return q_explore

        else:
            raise ValueError(f"{policy_type} is not a valid policy type.")
