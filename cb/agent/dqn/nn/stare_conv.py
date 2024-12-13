"""StarE Convolution Layer.

Paper: "Message Passing for Hyper-Relational Knowledge Graphs"
GitHub: https://github.com/migalkin/StarE
"""

from typing import Optional, Tuple

import torch
from torch_geometric.nn import MessagePassing
from torch_scatter import scatter_add

from .utils import rotate


class StarEConvLayer(MessagePassing):
    """StarE Convolution Layer.

    Implements the message passing for hyper-relational knowledge graphs.

    Attributes:
        in_channels (int): The number of input channels.
        out_channels (int): The number of output channels.
        num_rels (int): The number of relations.
        gcn_drop (float): The dropout probability.
        triple_qual_weight (float): The weight for the triple and qualifier embeddings.
        device (Optional[torch.device]): The device to use.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        num_rels: int,
        gcn_drop: float = 0.1,
        triple_qual_weight: float = 0.8,
    ):
        """Initialize the StarEConvLayer.

        Args:
            in_channels: The number of input channels.
            out_channels: The number of output channels.
            num_rels: The number of relations.
            gcn_drop: The dropout probability.
            triple_qual_weight: The weight for the triple and qualifier embeddings.
        """
        super(StarEConvLayer, self).__init__(flow="target_to_source", aggr="add")

        self.in_channels = in_channels
        self.out_channels = out_channels
        self.num_rels = num_rels
        self.device = None

        # Initialize weights
        self.w_loop = torch.nn.Parameter(torch.Tensor(in_channels, out_channels))
        self.w_in = torch.nn.Parameter(torch.Tensor(in_channels, out_channels))
        self.w_out = torch.nn.Parameter(torch.Tensor(in_channels, out_channels))
        self.w_rel = torch.nn.Parameter(torch.Tensor(in_channels, out_channels))
        self.w_q = torch.nn.Parameter(torch.Tensor(in_channels, in_channels))

        self.loop_rel = torch.nn.Parameter(torch.Tensor(1, in_channels))
        self.loop_ent = torch.nn.Parameter(torch.Tensor(1, in_channels))

        self.drop = torch.nn.Dropout(gcn_drop)
        self.bn = torch.nn.BatchNorm1d(out_channels)

        self.triple_qual_weight = triple_qual_weight

        self.reset_parameters()

    def reset_parameters(self) -> None:
        """Reset parameters using Xavier normal initialization."""
        torch.nn.init.xavier_normal_(self.w_loop)
        torch.nn.init.xavier_normal_(self.w_in)
        torch.nn.init.xavier_normal_(self.w_out)
        torch.nn.init.xavier_normal_(self.w_rel)
        torch.nn.init.xavier_normal_(self.w_q)
        torch.nn.init.xavier_normal_(self.loop_rel)
        torch.nn.init.xavier_normal_(self.loop_ent)

    def forward(
        self,
        entity_embeddings: torch.Tensor,
        relation_embeddings: torch.Tensor,
        edge_idx: torch.Tensor,
        edge_type: torch.Tensor,
        quals: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        """Perform forward pass of the StarE convolution layer.

        `entity_embeddings` is a tensor of shape [num_nodes, emb_dim], which is a stack
        of entity embeddings. Since x is a sampled sub-graph of the entire hidden graph,
        `num_nodes` is always less than the total number of global entities.
        `edge_idx` is a tensor of shape [2, num_edges] and `edge_type` is a tensor
        of shape [num_edges]. `relation_embeddings` is a tensor of shape
        [num_rels, emb_dim].


        Args:
            entity_embeddings: Node (the entities in a given graph) feature matrix.
            relation_embeddings: Relation embeddings.
            edge_idx: Graph edge indices.
            edge_type: Edge type indices.
            quals: Qualifier indices.

        Returns:
            Output node features and relation embeddings.
        """
        if self.device is None:
            self.device = edge_idx.device

        rel_embed = torch.cat([relation_embeddings, self.loop_rel], dim=0)
        num_edges = edge_idx.size(1) // 2
        num_ent = entity_embeddings.size(0)

        self.in_index, self.out_index = (
            edge_idx[:, :num_edges],
            edge_idx[:, num_edges:],
        )
        self.in_type, self.out_type = edge_type[:num_edges], edge_type[num_edges:]

        num_quals = quals.size(1) // 2
        self.in_index_qual_ent, self.out_index_qual_ent = (
            quals[1, :num_quals],
            quals[1, num_quals:],
        )
        self.in_index_qual_rel, self.out_index_qual_rel = (
            quals[0, :num_quals],
            quals[0, num_quals:],
        )
        self.quals_index_in, self.quals_index_out = (
            quals[2, :num_quals],
            quals[2, num_quals:],
        )

        # Self edges between all the nodes
        self.loop_index = torch.stack(
            [torch.arange(num_ent), torch.arange(num_ent)]
        ).to(self.device)
        self.loop_type = torch.full(
            (num_ent,), rel_embed.size(0) - 1, dtype=torch.long
        ).to(self.device)

        self.in_norm = self.compute_norm(self.in_index, num_ent)
        self.out_norm = self.compute_norm(self.out_index, num_ent)

        in_res = self.propagate(
            self.in_index,
            x=entity_embeddings,
            edge_type=self.in_type,
            rel_embed=rel_embed,
            edge_norm=self.in_norm,
            mode="in",
            ent_embed=entity_embeddings,
            qualifier_ent=self.in_index_qual_ent,
            qualifier_rel=self.in_index_qual_rel,
            qual_index=self.quals_index_in,
            source_index=self.in_index[0],
        )

        loop_res = self.propagate(
            self.loop_index,
            x=entity_embeddings,
            edge_type=self.loop_type,
            rel_embed=rel_embed,
            edge_norm=None,
            mode="loop",
            ent_embed=None,
            qualifier_ent=None,
            qualifier_rel=None,
            qual_index=None,
            source_index=None,
        )
        out_res = self.propagate(
            self.out_index,
            x=entity_embeddings,
            edge_type=self.out_type,
            rel_embed=rel_embed,
            edge_norm=self.out_norm,
            mode="out",
            ent_embed=entity_embeddings,
            qualifier_ent=self.out_index_qual_ent,
            qualifier_rel=self.out_index_qual_rel,
            qual_index=self.quals_index_out,
            source_index=self.out_index[0],
        )

        out = (
            self.drop(in_res) * (1 / 3)
            + self.drop(out_res) * (1 / 3)
            + loop_res * (1 / 3)
        )

        out = self.bn(out)

        # Ignoring the self loop inserted, return.
        return torch.tanh(out), torch.matmul(rel_embed, self.w_rel)[:-1]

    def rel_transform(
        self, ent_embed: torch.Tensor, rel_embed: torch.Tensor
    ) -> torch.Tensor:
        """Transform entity embeddings using relation embeddings.

        Args:
            ent_embed: Entity embeddings.
            rel_embed: Relation embeddings.

        Returns:
            Transformed entity embeddings.
        """
        trans_embed = rotate(ent_embed, rel_embed)
        return trans_embed

    def qual_transform(
        self, qualifier_ent: torch.Tensor, qualifier_rel: torch.Tensor
    ) -> torch.Tensor:
        """Transform qualifier embeddings.

        Args:
            qualifier_ent: Qualifier entity embeddings.
            qualifier_rel: Qualifier relation embeddings.

        Returns:
            Transformed qualifier embeddings.
        """
        trans_embed = rotate(qualifier_ent, qualifier_rel)
        return trans_embed

    def qualifier_aggregate(
        self,
        qualifier_emb: torch.Tensor,
        rel_part_emb: torch.Tensor,
        alpha: float,
        qual_index: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Aggregate qualifier embeddings.

        Args:
            qualifier_emb: Qualifier embeddings.
            rel_part_emb: Relation part embeddings.
            alpha: Weight factor for aggregation.
            qual_index: Qualifier indices.

        Returns:
            Aggregated embeddings.
        """
        qualifier_emb = torch.einsum(
            "ij,jk -> ik",
            self.coalesce_quals(qualifier_emb, qual_index, rel_part_emb.shape[0]),
            self.w_q,
        )

        return alpha * rel_part_emb + (1 - alpha) * qualifier_emb

    def update_rel_emb_with_qualifier(
        self,
        ent_embed: torch.Tensor,
        rel_embed: torch.Tensor,
        qualifier_ent: torch.Tensor,
        qualifier_rel: torch.Tensor,
        edge_type: torch.Tensor,
        qual_index: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Update relation embeddings with qualifier embeddings.

        Args:
            ent_embed: Entity embeddings.
            rel_embed: Relation embeddings.
            qualifier_ent: Qualifier entity embeddings.
            qualifier_rel: Qualifier relation embeddings.
            edge_type: Edge type indices.
            qual_index: Qualifier indices.

        Returns:
            Updated relation embeddings.
        """

        # Step 1: embedding
        qualifier_emb_rel = rel_embed[qualifier_rel]
        qualifier_emb_ent = ent_embed[qualifier_ent]

        rel_part_emb = rel_embed[edge_type]

        # Step 2: pass it through qual_transform
        qualifier_emb = self.qual_transform(
            qualifier_ent=qualifier_emb_ent, qualifier_rel=qualifier_emb_rel
        )

        # Pass it through an aggregate layer
        return self.qualifier_aggregate(
            qualifier_emb,
            rel_part_emb,
            alpha=self.triple_qual_weight,
            qual_index=qual_index,
        )

    def message(
        self,
        x_j: torch.Tensor,
        x_i: torch.Tensor,
        edge_type: torch.Tensor,
        rel_embed: torch.Tensor,
        edge_norm: Optional[torch.Tensor],
        mode: str,
        ent_embed: Optional[torch.Tensor] = None,
        qualifier_ent: Optional[torch.Tensor] = None,
        qualifier_rel: Optional[torch.Tensor] = None,
        qual_index: Optional[torch.Tensor] = None,
        source_index: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        """Construct messages for message passing.

        Args:
            x_j: Source node features.
            x_i: Target node features.
            edge_type: Edge type indices.
            rel_embed: Relation embeddings.
            edge_norm: Edge normalization coefficients.
            mode (str): Mode of message passing (in, out, loop).
            ent_embed: Entity embeddings.
            qualifier_ent: Qualifier entity embeddings.
            qualifier_rel: Qualifier relation embeddings.
            qual_index: Qualifier indices.
            source_index: Source node indices.

        Returns:
            Messages for aggregation.
        """
        weight = getattr(self, "w_{}".format(mode))

        if mode != "loop":
            rel_emb = self.update_rel_emb_with_qualifier(
                ent_embed,
                rel_embed,
                qualifier_ent,
                qualifier_rel,
                edge_type,
                qual_index,
            )
        else:
            rel_emb = torch.index_select(rel_embed, 0, edge_type)

        xj_rel = self.rel_transform(x_j, rel_emb)
        out = torch.einsum("ij,jk->ik", xj_rel, weight)

        return out if edge_norm is None else out * edge_norm.view(-1, 1)

    def update(self, aggr_out: torch.Tensor, mode: str) -> torch.Tensor:
        """Update node features after aggregation.

        Args:
            aggr_out: Aggregated messages.
            mode: Mode of message passing.

        Returns:
            Updated node features.
        """
        return aggr_out

    @staticmethod
    def compute_norm(edge_idx: torch.Tensor, num_ent: int) -> torch.Tensor:
        """Compute normalization coefficients for edges.

        Args:
            edge_idx: Edge indices.
            num_ent: Number of entities.

        Returns:
            Normalization coefficients.
        """
        row, col = edge_idx
        edge_weight = torch.ones_like(row).float()
        deg = scatter_add(edge_weight, row, dim=0, dim_size=num_ent)
        deg_inv = deg.pow(-0.5)
        deg_inv[deg_inv == float("inf")] = 0
        norm = deg_inv[row] * edge_weight * deg_inv[col]
        return norm

    def coalesce_quals(
        self,
        qual_embeddings: torch.Tensor,
        qual_index: torch.Tensor,
        num_edges: int,
        fill: int = 0,
    ) -> torch.Tensor:
        """Coalesce qualifier embeddings.

        Args:
            qual_embeddings: Qualifier embeddings.
            qual_index: Qualifier indices.
            num_edges: Number of edges.
            fill: Fill value for empty embeddings. Default is 0.

        Returns:
            Coalesced qualifier embeddings.
        """
        output = scatter_add(qual_embeddings, qual_index, dim=0, dim_size=num_edges)

        if fill != 0:
            mask = output.sum(dim=-1) == 0
            output[mask] = fill

        return output

    def __repr__(self) -> str:
        """Return a string representation of the layer."""
        return (
            f"{self.__class__.__name__}({self.in_channels}, {self.out_channels}, "
            f"num_rels={self.num_rels})"
        )
