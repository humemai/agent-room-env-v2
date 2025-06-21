"""Transformer-based function approximator for DQN memory management."""

from typing import Any

import numpy as np
import torch
import torch.nn as nn

from .attention import AttentionAggregator
from .mlp import MLP


class MemoryTokenizer(nn.Module):
    """Tokenizes memory quadruples into vector representations.

    Converts (head, relation, tail, qualifiers) into a single token vector
    by concatenating embeddings and qualifier information.
    """

    def __init__(
        self,
        entities: list[str],
        relations: list[str],
        embedding_dim: int,
        device: str = "cpu",
    ):
        super().__init__()
        self.entities = entities
        self.relations = relations
        self.embedding_dim = embedding_dim
        self.device = device

        # Create entity and relation mappings
        self.entity_to_idx = {entity: idx for idx, entity in enumerate(entities)}
        self.relation_to_idx = {relation: idx for idx, relation in enumerate(relations)}

        # Entity and relation embeddings
        self.entity_embeddings = nn.Parameter(
            torch.Tensor(len(entities), embedding_dim)
        ).to(device)
        self.relation_embeddings = nn.Parameter(
            torch.Tensor(len(relations), embedding_dim)
        ).to(device)

        # MLP for processing individual qualifier key-value pairs
        self.qualifier_mlp = MLP(
            n_actions=embedding_dim,  # Output dimension
            input_size=embedding_dim * 2,  # type_emb + value_emb
            hidden_size=embedding_dim,
            device=device,
            num_hidden_layers=1,
            dueling_dqn=False,
        )

        # Attention aggregator for combining multiple qualifiers
        self.qualifier_attention = AttentionAggregator(
            embedding_dim=embedding_dim,
            device=device,
        )

        # Linear projection to combine all information into final token
        self.token_projection = nn.Linear(
            embedding_dim * 4,  # head + relation + tail + qualifier_info
            embedding_dim,
            device=device,
        )

        self._init_parameters()

    def _init_parameters(self):
        """Initialize parameters with Xavier normal."""
        nn.init.xavier_normal_(self.entity_embeddings)
        nn.init.xavier_normal_(self.relation_embeddings)
        nn.init.xavier_normal_(self.token_projection.weight)
        if self.token_projection.bias is not None:
            self.token_projection.bias.data.zero_()

    def forward(self, memory_batch: list[list]) -> torch.Tensor:
        """Convert memory quadruples to token vectors.

        Args:
            memory_batch: list of memory samples, where each sample is a list of
                         quadruples [head, relation, tail, qualifiers]

        Returns:
            Tokenized memories: (total_memories_in_batch, embedding_dim)
        """
        # Flatten and validate all quadruples first
        all_quadruples = []
        for sample in memory_batch:
            for quadruple in sample:
                head, relation, tail, qualifiers = quadruple

                # Validate entities and relations exist
                if head not in self.entity_to_idx:
                    raise ValueError(f"Unknown entity '{head}' in entities")
                if relation not in self.relation_to_idx:
                    raise ValueError(f"Unknown relation '{relation}' in relations")
                if tail not in self.entity_to_idx:
                    raise ValueError(f"Unknown entity '{tail}' in entities")

                # Validate that at least one valid qualifier exists (excluding memory_id)
                valid_qualifiers = {
                    k: v for k, v in qualifiers.items() if k != "memory_id"
                }
                if not valid_qualifiers:
                    raise ValueError(
                        f"Quadruple ({head}, {relation}, {tail}) has no valid qualifiers. "
                        "Every memory must have at least one qualifier (excluding memory_id)."
                    )

                all_quadruples.append((head, relation, tail, qualifiers))

        if not all_quadruples:
            raise ValueError(
                "No valid quadruples found in the memory batch. "
                "At least one quadruple is required."
            )

        # Batch process all qualifiers and get embeddings
        qualifier_embeddings = self._batch_process_qualifiers(all_quadruples)

        # Batch process head, relation, tail embeddings
        heads, relations, tails = zip(*[(q[0], q[1], q[2]) for q in all_quadruples])

        head_indices = torch.tensor(
            [self.entity_to_idx[h] for h in heads], device=self.device
        )
        rel_indices = torch.tensor(
            [self.relation_to_idx[r] for r in relations], device=self.device
        )
        tail_indices = torch.tensor(
            [self.entity_to_idx[t] for t in tails], device=self.device
        )

        head_embs = self.entity_embeddings[
            head_indices
        ]  # (n_quadruples, embedding_dim)
        rel_embs = self.relation_embeddings[
            rel_indices
        ]  # (n_quadruples, embedding_dim)
        tail_embs = self.entity_embeddings[
            tail_indices
        ]  # (n_quadruples, embedding_dim)

        # Concatenate all embeddings
        token_inputs = torch.cat(
            [head_embs, rel_embs, tail_embs, qualifier_embeddings], dim=1
        )

        # Project to final tokens
        tokens = self.token_projection(token_inputs)

        return tokens

    def _batch_process_qualifiers(self, all_quadruples: list) -> torch.Tensor:
        """Batch process all qualifiers from all quadruples."""
        # First pass: collect all qualifiers and track their quadruple assignment
        all_type_indices = []
        all_value_indices = []
        qualifier_to_quad_map = []  # Maps each qualifier to its quadruple index
        quad_qualifier_counts = []  # Number of qualifiers per quadruple

        for quad_idx, (_, _, _, qualifiers) in enumerate(all_quadruples):
            valid_quals = 0
            for qual_key, qual_value in qualifiers.items():
                if qual_key == "memory_id":
                    continue

                # Validate qualifier key and value
                if qual_key not in self.relation_to_idx:
                    raise ValueError(
                        f"Unknown qualifier type '{qual_key}' in relations"
                    )

                qual_value_str = str(qual_value)
                if qual_value_str not in self.entity_to_idx:
                    raise ValueError(
                        f"Unknown qualifier value '{qual_value_str}' in entities"
                    )

                all_type_indices.append(self.relation_to_idx[qual_key])
                all_value_indices.append(self.entity_to_idx[qual_value_str])
                qualifier_to_quad_map.append(quad_idx)
                valid_quals += 1

            if valid_quals == 0:
                raise ValueError(
                    f"Quadruple {quad_idx} has no valid qualifiers (excluding memory_id). "
                    "Every memory must have at least one qualifier."
                )
            quad_qualifier_counts.append(valid_quals)

        if not all_type_indices:
            raise ValueError("No valid qualifiers found across all quadruples")

        # Batch process all qualifiers through MLP
        type_indices = torch.tensor(all_type_indices, device=self.device)
        value_indices = torch.tensor(all_value_indices, device=self.device)

        type_embs = self.relation_embeddings[
            type_indices
        ]  # (total_quals, embedding_dim)
        value_embs = self.entity_embeddings[
            value_indices
        ]  # (total_quals, embedding_dim)

        combined_inputs = torch.cat(
            [type_embs, value_embs], dim=1
        )  # (total_quals, embedding_dim * 2)
        processed_qualifiers = self.qualifier_mlp(
            combined_inputs
        )  # (total_quals, embedding_dim)

        # Group qualifiers by quadruple and apply attention
        aggregated_qualifiers = []
        qual_start_idx = 0

        for num_quals in quad_qualifier_counts:
            # Get qualifiers for this quadruple
            quad_quals = processed_qualifiers[
                qual_start_idx : qual_start_idx + num_quals
            ]
            qual_start_idx += num_quals

            # Apply attention aggregation with proper masking
            quad_quals_batch = quad_quals.unsqueeze(0)  # (1, num_quals, embedding_dim)
            # Attention mask: True for valid positions (our convention)
            attention_mask = torch.ones(
                1, num_quals, dtype=torch.bool, device=self.device
            )

            aggregated = self.qualifier_attention(quad_quals_batch, attention_mask)
            aggregated_qualifiers.append(aggregated.squeeze(0))  # (embedding_dim,)

        return torch.stack(aggregated_qualifiers)  # (n_quadruples, embedding_dim)

    def _process_qualifiers(self, qualifiers: dict[str, Any]) -> torch.Tensor:
        """Process qualifiers into a single embedding vector using MLP +
        AttentionAggregator."""
        qualifier_embeddings = []

        for qual_key, qual_value in qualifiers.items():
            # Skip memory_id as it's only for symbolic reasoning
            if qual_key == "memory_id":
                continue

            # Get type embedding from relations (qualifier relations are already included)
            if qual_key not in self.relation_to_idx:
                raise ValueError(
                    f"Unknown qualifier type '{qual_key}' in relations: {self.relations}"
                )

            type_emb = self.relation_embeddings[self.relation_to_idx[qual_key]]

            # Get value embedding (convert value to string and look up in entities)
            qual_value_str = str(qual_value)
            if qual_value_str not in self.entity_to_idx:
                raise ValueError(
                    f"Unknown qualifier value '{qual_value_str}' in entities"
                )
            value_emb = self.entity_embeddings[self.entity_to_idx[qual_value_str]]

            # Combine type and value embeddings through MLP
            combined_input = torch.cat(
                [type_emb, value_emb], dim=0
            )  # (embedding_dim * 2,)
            processed_qualifier = self.qualifier_mlp(
                combined_input.unsqueeze(0)
            )  # (1, embedding_dim)
            qualifier_embeddings.append(processed_qualifier.squeeze(0))

        if not qualifier_embeddings:
            raise ValueError(
                "No valid qualifiers found in the quadruple (excluding memory_id). "
                "Every memory must have at least one qualifier."
            )

        # Always use attention aggregation, even for single qualifier
        # Stack qualifiers and add dummy batch dimension
        stacked_qualifiers = torch.stack(qualifier_embeddings).unsqueeze(
            0
        )  # (1, num_quals, embedding_dim)

        # Create mask (True for valid positions - our convention)
        mask = torch.ones(
            1, len(qualifier_embeddings), dtype=torch.bool, device=self.device
        )

        # Apply attention aggregation
        aggregated = self.qualifier_attention(
            stacked_qualifiers, mask
        )  # (1, embedding_dim)

        return aggregated.squeeze(0)  # (embedding_dim,)


class TransformerMemoryEncoder(nn.Module):
    """Multi-layer Transformer encoder for memory sequences."""

    def __init__(
        self,
        embedding_dim: int,
        dim_feedforward: int,  # Typically 4x embedding_dim
        num_layers: int = 2,
        num_heads: int = 8,
        dropout: float = 0.1,
        device: str = "cpu",
    ):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.num_layers = num_layers
        self.device = device

        # Transformer encoder layers
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embedding_dim,
            nhead=num_heads,
            dim_feedforward=dim_feedforward,  # Typically 4x embedding_dim
            dropout=dropout,
            batch_first=True,
            device=device,
        )

        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer, num_layers=num_layers
        ).to(device)

    def forward(
        self, token_embeddings: torch.Tensor, padding_mask: torch.Tensor = None
    ) -> torch.Tensor:
        """Apply transformer encoding to memory tokens.

        Args:
            token_embeddings: (batch_size, seq_len, embedding_dim)
            padding_mask: (batch_size, seq_len) - True for padded positions (PyTorch convention)

        Returns:
            Encoded embeddings: (batch_size, seq_len, embedding_dim)
        """
        return self.transformer_encoder(
            token_embeddings, src_key_padding_mask=padding_mask
        )


class TransformerMemoryNet(nn.Module):
    """Complete Transformer-based memory management network."""

    def __init__(
        self,
        entities: list[str],
        relations: list[str],
        embedding_dim: int = 64,
        dim_feedforward: int = 256,  # Typically 4x embedding_dim
        num_transformer_layers: int = 2,
        num_heads: int = 8,
        dropout: float = 0.1,
        mlp_params: dict = {"num_hidden_layers": 2, "dueling_dqn": True},
        device: str = "cpu",
        forget_needs_rl: bool = True,
        remember_needs_rl: bool = True,
        separate_network_type: str = None,
    ):
        super().__init__()
        self.device = device
        self.embedding_dim = embedding_dim
        self.dim_feedforward = dim_feedforward
        self.forget_needs_rl = forget_needs_rl
        self.remember_needs_rl = remember_needs_rl
        self.separate_network_type = separate_network_type

        # Memory tokenizer
        self.tokenizer = MemoryTokenizer(
            entities=entities,
            relations=relations,
            embedding_dim=embedding_dim,
            device=device,
        )

        # Transformer encoder
        self.transformer = TransformerMemoryEncoder(
            embedding_dim=embedding_dim,
            dim_feedforward=dim_feedforward,
            num_layers=num_transformer_layers,
            num_heads=num_heads,
            dropout=dropout,
            device=device,
        )

        # Policy-specific components based on network type
        if separate_network_type == "forget":
            self.attention_aggregator_forget = AttentionAggregator(
                embedding_dim=embedding_dim,
                device=device,
            )
            self.mlp_forget = MLP(
                n_actions=3,  # lru, lfu, fifo
                input_size=embedding_dim,
                hidden_size=embedding_dim,
                device=device,
                **mlp_params,
            )
        elif separate_network_type == "remember":
            self.mlp_remember = MLP(
                n_actions=2,  # remember, forget
                input_size=embedding_dim,
                hidden_size=embedding_dim,
                device=device,
                **mlp_params,
            )
        else:
            # Shared network
            if forget_needs_rl:
                self.attention_aggregator_forget = AttentionAggregator(
                    embedding_dim=embedding_dim,
                    device=device,
                )
                self.mlp_forget = MLP(
                    n_actions=3,
                    input_size=embedding_dim,
                    hidden_size=embedding_dim,
                    device=device,
                    **mlp_params,
                )

            if remember_needs_rl:
                self.mlp_remember = MLP(
                    n_actions=2,
                    input_size=embedding_dim,
                    hidden_size=embedding_dim,
                    device=device,
                    **mlp_params,
                )

        self.to(device)

    def _prepare_batch_data(self, data: np.ndarray):
        """Prepare batched data for transformer processing."""
        # Extract short-term memory information
        batch_info = []
        all_memories = []

        for sample in data:
            short_term_memories = []
            all_sample_memories = []

            for i, quadruple in enumerate(sample):
                head, relation, tail, qualifiers = quadruple
                all_sample_memories.append(quadruple)

                # Check if it's short-term memory (has current_time qualifier)
                if "current_time" in qualifiers:
                    short_term_memories.append(i)

            # Validate that we have at least one memory with qualifiers
            if not all_sample_memories:
                raise ValueError("Sample contains no memories")

            batch_info.append(
                {
                    "short_term_indices": short_term_memories,
                    "total_memories": len(all_sample_memories),
                }
            )
            all_memories.append(all_sample_memories)

        return all_memories, batch_info

    def forward(self, data: np.ndarray, policy_type: str) -> list[torch.Tensor]:
        """Forward pass for memory management policies.

        Args:
            data: Batch of memory samples
            policy_type: 'remember' or 'forget'

        Returns:
            list of Q-value tensors for each sample in the batch
        """
        # Validate policy type
        if self.separate_network_type == "forget" and policy_type != "forget":
            raise ValueError(
                f"This network is configured for forget policy only, got {policy_type}"
            )
        if self.separate_network_type == "remember" and policy_type != "remember":
            raise ValueError(
                f"This network is configured for remember policy only, got {policy_type}"
            )

        if policy_type == "remember" and not hasattr(self, "mlp_remember"):
            raise ValueError("Remember policy components not available in this network")
        if policy_type == "forget" and not hasattr(self, "mlp_forget"):
            raise ValueError("Forget policy components not available in this network")

        all_memories, batch_info = self._prepare_batch_data(data)

        # Tokenize all memories (this will validate qualifier requirements)
        all_tokens = self.tokenizer(all_memories)  # (total_memories, embedding_dim)

        # Prepare batched input for transformer
        max_memories = max(info["total_memories"] for info in batch_info)
        batch_size = len(batch_info)

        # Create padded batch tensor
        padded_tokens = torch.zeros(
            batch_size, max_memories, self.embedding_dim, device=self.device
        )
        padding_mask = torch.ones(
            batch_size, max_memories, dtype=torch.bool, device=self.device
        )

        # Fill padded tensor
        token_idx = 0
        for i, info in enumerate(batch_info):
            num_memories = info["total_memories"]
            if num_memories > 0:
                padded_tokens[i, :num_memories] = all_tokens[
                    token_idx : token_idx + num_memories
                ]
                # Set False for valid positions (PyTorch transformer convention)
                padding_mask[i, :num_memories] = False
            token_idx += num_memories

        # Apply transformer encoding
        encoded_tokens = self.transformer(
            padded_tokens, padding_mask
        )  # (batch_size, max_memories, embedding_dim)

        if policy_type == "remember":
            return self._handle_remember_policy(
                encoded_tokens, batch_info, padding_mask
            )
        else:
            return self._handle_forget_policy(encoded_tokens, padding_mask)

    def _handle_remember_policy(self, encoded_tokens, batch_info, padding_mask):
        """Handle remember policy Q-value computation."""
        q_remember_batch = []

        for i, info in enumerate(batch_info):
            short_term_indices = info["short_term_indices"]

            if not short_term_indices:
                raise ValueError(
                    f"Sample {i} has no short-term memories for remember policy"
                )

            # Extract short-term memory tokens
            short_term_tokens = encoded_tokens[
                i, short_term_indices
            ]  # (num_short_term, embedding_dim)

            # Apply MLP to each short-term memory token
            q_values = self.mlp_remember(short_term_tokens)  # (num_short_term, 2)
            q_remember_batch.append(q_values)

        return q_remember_batch

    def _handle_forget_policy(self, encoded_tokens, padding_mask):
        """Handle forget policy Q-value computation."""
        # Use attention aggregator to get single representation per sample
        # Convert padding mask to attention mask (invert for our attention convention)
        attention_mask = ~padding_mask  # True for valid positions, False for padded

        aggregated_embeddings = self.attention_aggregator_forget(
            encoded_tokens, attention_mask
        )  # (batch_size, embedding_dim)

        # Apply MLP for forget policy
        q_forget = self.mlp_forget(aggregated_embeddings)  # (batch_size, 3)

        # Convert to list format for consistency
        return [q_forget[i : i + 1] for i in range(q_forget.size(0))]
