"""Attention module for memory management forget policy."""

import torch
import torch.nn.functional as F


class AttentionAggregator(torch.nn.Module):
    """Attention-based aggregation for memory management forget policy.

    This module uses a learnable query vector to attend over node embeddings and
    aggregate them for the forget policy decision. The aggregation follows the
    transformer attention mechanism with linear projections for keys and values.

    Attributes:
        embedding_dim: Dimension of the input embeddings
        device: Device to use for computations
        query: Learnable query vector
        key_projection: Linear layer to project embeddings to keys
        value_projection: Linear layer to project embeddings to values
    """

    def __init__(
        self,
        embedding_dim: int,
        device: str = "cpu",
    ) -> None:
        """Initialize the attention aggregator.

        Args:
            embedding_dim: Dimension of the input embeddings
            device: Device to use for computations
        """
        super(AttentionAggregator, self).__init__()
        self.embedding_dim = embedding_dim
        self.device = device

        # Learnable query vector
        self.query = torch.nn.Parameter(torch.Tensor(1, embedding_dim)).to(self.device)
        torch.nn.init.xavier_normal_(self.query)

        # Linear projections for keys and values
        self.key_projection = torch.nn.Linear(
            embedding_dim, embedding_dim, device=self.device
        )
        self.value_projection = torch.nn.Linear(
            embedding_dim, embedding_dim, device=self.device
        )

        # Apply Xavier initialization
        torch.nn.init.xavier_normal_(self.key_projection.weight)
        torch.nn.init.xavier_normal_(self.value_projection.weight)
        if self.key_projection.bias is not None:
            self.key_projection.bias.data.zero_()
        if self.value_projection.bias is not None:
            self.value_projection.bias.data.zero_()

    def forward(
        self, node_embeddings: torch.Tensor, mask: torch.Tensor = None
    ) -> torch.Tensor:
        """Forward pass of the attention aggregator.

        Args:
            node_embeddings: Node embeddings after GNN layers.
                Shape: (batch_size, max_num_nodes, embedding_dim) for batched input
                       (num_nodes, embedding_dim) for single sample
            mask: Attention mask for padded positions.
                Shape: (batch_size, max_num_nodes) for batched input
                       None for single sample

        Returns:
            Aggregated embedding for forget policy decision.
            Shape: (batch_size, embedding_dim) for batched input
                   (embedding_dim,) for single sample
        """
        # Handle both single sample and batched inputs
        if node_embeddings.dim() == 2:  # Single sample: (num_nodes, embedding_dim)
            return self._forward_single(node_embeddings)
        else:  # Batched: (batch_size, max_num_nodes, embedding_dim)
            return self._forward_batch(node_embeddings, mask)

    def _forward_single(self, node_embeddings: torch.Tensor) -> torch.Tensor:
        """Forward pass for single sample (original behavior)."""
        # Project embeddings to keys and values
        keys = self.key_projection(node_embeddings)  # (num_nodes, embedding_dim)
        values = self.value_projection(node_embeddings)  # (num_nodes, embedding_dim)

        # Compute attention scores: query @ keys^T
        # query: (1, embedding_dim), keys: (num_nodes, embedding_dim)
        attention_scores = torch.matmul(
            self.query, keys.transpose(0, 1)
        )  # (1, num_nodes)

        # Scale by sqrt(embedding_dim) as in transformer
        attention_scores = attention_scores / (self.embedding_dim**0.5)

        # Apply softmax to get attention weights
        attention_weights = F.softmax(attention_scores, dim=-1)  # (1, num_nodes)

        # Weighted sum of values
        aggregated_embedding = torch.matmul(
            attention_weights, values
        )  # (1, embedding_dim)

        return aggregated_embedding.squeeze(0)  # (embedding_dim,)

    def _forward_batch(
        self, node_embeddings: torch.Tensor, mask: torch.Tensor
    ) -> torch.Tensor:
        """Forward pass for batched input with padding and masking."""
        batch_size, max_num_nodes, embedding_dim = node_embeddings.shape

        # Project embeddings to keys and values
        keys = self.key_projection(
            node_embeddings
        )  # (batch_size, max_num_nodes, embedding_dim)
        values = self.value_projection(
            node_embeddings
        )  # (batch_size, max_num_nodes, embedding_dim)

        # Expand query for batch processing
        query_batch = self.query.expand(batch_size, -1)  # (batch_size, embedding_dim)

        # Compute attention scores: batch_query @ keys^T
        attention_scores = torch.bmm(
            query_batch.unsqueeze(1),  # (batch_size, 1, embedding_dim)
            keys.transpose(1, 2),  # (batch_size, embedding_dim, max_num_nodes)
        ).squeeze(
            1
        )  # (batch_size, max_num_nodes)

        # Scale by sqrt(embedding_dim)
        attention_scores = attention_scores / (self.embedding_dim**0.5)

        # Apply mask to attention scores (set padded positions to -inf)
        if mask is not None:
            attention_scores = attention_scores.masked_fill(~mask, float("-inf"))

        # Apply softmax to get attention weights
        attention_weights = F.softmax(
            attention_scores, dim=-1
        )  # (batch_size, max_num_nodes)

        # Handle case where all positions are masked (shouldn't happen in practice)
        attention_weights = torch.nan_to_num(attention_weights, nan=0.0)

        # Weighted sum of values
        aggregated_embedding = torch.bmm(
            attention_weights.unsqueeze(1),  # (batch_size, 1, max_num_nodes)
            values,  # (batch_size, max_num_nodes, embedding_dim)
        ).squeeze(
            1
        )  # (batch_size, embedding_dim)

        return aggregated_embedding
