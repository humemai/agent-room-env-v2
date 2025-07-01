import os
from copy import deepcopy
from datetime import timedelta
from typing import Any

import gymnasium as gym
import numpy as np
import torch
import torch.optim as optim
from rdflib import XSD, Literal, URIRef

from .long import LongTermAgent
from .nn import GNN
from .utils import (ReplayBuffer, plot_results, save_final_results,
                    save_states_q_values_actions, save_validation,
                    select_action, target_hard_update, update_epsilon,
                    update_model, write_yaml)


class DQNAgent(LongTermAgent):
    """
    DQNAgent is a specialized LongTermAgent that uses Deep Q-Learning for decision
    making. It inherits from LongTermAgent and implements the DQN algorithm.

    Now supports both GNN and Transformer-based function approximators.
    """

    def __init__(
        self,
        env_str: str = "room_env:RoomEnv-v2",
        env_config: dict[str, Any] = {
            "question_prob": 1.0,
            "terminates_at": 99,
            "randomize_observations": "all",
            "room_size": "xl-different-prob",
            "rewards": {"correct": 1, "wrong": 0, "partial": 0},
            "make_everything_static": False,
            "num_total_questions": 1000,
            "question_interval": 1,
            "include_walls_in_observations": True,
            "deterministic_objects": False,
        },
        qa_policy: str = "most_recently_added",
        explore_policy: str = "dijkstra",
        forget_policy: str = "lru",
        remember_policy: str = "all",
        max_long_term_memory_size: int = 100,
        num_samples_for_results: dict = {"val": 5, "test": 10},
        save_results: bool = True,
        default_root_dir: str = "./training-results/",
        num_iterations: int = 10000,
        replay_buffer_size: int = 1000,
        warm_start: int = 32,
        batch_size: int = 32,
        target_update_interval: int = 10,
        epsilon_decay_until: float = 10000,
        max_epsilon: float = 1.0,
        min_epsilon: float = 0.01,
        gamma: dict = 0.99,
        learning_rate: int = 0.001,
        architecture_type: str = "stare",  # "stare", "gcn", or "transformer"
        stare_params: dict = {
            "embedding_dim": 64,
            "num_layers": 2,
            "gcn_drop": 0.1,
            "triple_qual_weight": 0.8,
            "silu_between_layers": True,
            "dropout_between_layers": True,
        },
        gcn_params: dict = {
            "embedding_dim": 64,
            "num_layers": 2,
            "gcn_drop": 0.1,
            "silu_between_layers": True,
            "dropout_between_layers": True,
        },
        transformer_params: dict = {
            "embedding_dim": 64,
            "num_layers": 2,
            "dim_feedforward": 256,  # typically 4 * embedding_dim
            "num_heads": 8,
            "dropout": 0.1,
        },
        mlp_params: dict = {"num_hidden_layers": 2, "dueling_dqn": True},
        validation_interval: int = 5,
        plotting_interval: int = 20,
        train_seed: int = 5,
        test_seed: int = 0,
        device: str = "cpu",
        ddqn: bool = True,
        pretrain_semantic: str | bool = False,
        use_gradient_clipping: bool = True,
        gradient_clip_value: float = 1.0,
        separate_networks: bool = False,
    ) -> None:
        r"""Initialize the DQNAgent.
        Args:
            env_str: The name of the environment to use.
            env_config: A dictionary containing the environment configuration.
            qa_policy: The policy to use for answering questions.
            explore_policy: The policy to use for exploration.
            forget_policy: The policy to use when the long-term memory is full.
            remember_policy: The policy to use when we have to move from short-term
                to long-term.
            max_long_term_memory_size: The maximum size of the long-term memory.
            num_samples_for_results: A dictionary containing the number of samples for
                validation and testing.
            save_results: Whether to save the results to disk.
            default_root_dir: The root directory to store the results.
            num_iterations: The number of training iterations.
            replay_buffer_size: The size of the replay buffer.
            warm_start: The number of warm start samples before training.
            batch_size: The batch size for training.
            target_update_interval: The interval for updating the target network.
            epsilon_decay_until: The number of iterations until epsilon decays to
                min_epsilon.
            max_epsilon: The maximum value of epsilon for exploration.
            min_epsilon: The minimum value of epsilon for exploration.
            gamma: The discount factor for future rewards.
            learning_rate: The learning rate for the optimizer.
            architecture_type: The type of architecture to use: "stare", "gcn", or "transformer"
            stare_params: Parameters specific to StarE architecture
            gcn_params: Parameters specific to vanilla GCN architecture
            transformer_params: Parameters specific to Transformer architecture
            mlp_params: Parameters for the MLP heads (shared across architectures)
            validation_interval: The interval for validation during training.
            plotting_interval: The interval for plotting the results.
            train_seed: The seed for the training environment.
            test_seed: The seed for the testing environment.
            device: The device to use for training (e.g., "cpu" or "cuda").
            ddqn: Whether to use Double DQN.
            pretrain_semantic: Whether to pretrain the semantic memory.
                False, "exclude_walls", "include_walls"
            use_gradient_clipping: Whether to use gradient clipping during training.
            gradient_clip_value: The maximum norm for gradient clipping.
            separate_networks: Whether to use separate networks for remember and forget
                policies.

        """
        env_config["seed"] = train_seed
        params_to_save = deepcopy(locals())
        del params_to_save["self"]
        del params_to_save["__class__"]

        super().__init__(**params_to_save)

        # Validate architecture type
        valid_architectures = ["stare", "gcn", "transformer"]
        if architecture_type.lower() not in valid_architectures:
            raise ValueError(
                f"architecture_type must be one of {valid_architectures}, got {architecture_type}"
            )

        self.architecture_type = architecture_type.lower()
        self.stare_params = stare_params
        self.gcn_params = gcn_params
        self.transformer_params = transformer_params
        self.mlp_params = mlp_params

        self.num_iterations = num_iterations
        self.replay_buffer_size = replay_buffer_size
        self.warm_start = warm_start
        self.batch_size = batch_size
        self.target_update_interval = target_update_interval
        self.epsilon_decay_until = epsilon_decay_until
        self.epsilon = max_epsilon
        self.max_epsilon = max_epsilon
        self.min_epsilon = min_epsilon
        self.gamma = gamma
        self.learning_rate = learning_rate
        self.validation_interval = validation_interval
        self.plotting_interval = plotting_interval
        self.train_seed = train_seed
        self.test_seed = test_seed
        self.device = device
        self.ddqn = ddqn
        self.pretrain_semantic = pretrain_semantic
        self.use_gradient_clipping = use_gradient_clipping
        self.gradient_clip_value = gradient_clip_value
        self.val_file_names = []

        assert self.batch_size <= self.warm_start <= self.replay_buffer_size

        self.forget2str = {0: "fifo", 1: "lru", 2: "lfu"}
        self.remember2str = {0: "remember", 1: "forget"}
        self.qa2str = {
            0: "most_recently_added",
            1: "most_recently_used",
            2: "most_frequently_used",
        }
        self.explore2str = {0: "dijkstra", 1: "bfs"}

        self.forget2int = {v: k for k, v in self.forget2str.items()}
        self.remember2int = {v: k for k, v in self.remember2str.items()}
        self.qa2int = {v: k for k, v in self.qa2str.items()}
        self.explore2int = {v: k for k, v in self.explore2str.items()}

        # Prepare parameters for GNN initialization
        gnn_params = {
            "device": self.device,
            "entities": [
                e for entities in self.env.unwrapped.entities.values() for e in entities
            ]
            + ["user"]
            + [str(i) for i in range(env_config["terminates_at"] * 2)]
            + [
                (self.base_date + timedelta(days=i)).isoformat(timespec="seconds")
                for i in range(env_config["terminates_at"] + 2)
            ],
            "relations": (
                self.env.unwrapped.relations
                + [rel + "_inv" for rel in self.env.unwrapped.relations]
                + [
                    "current_time",
                    "time_added",
                    "last_accessed",
                    "num_recalled",
                    "derived_from",
                ]
            ),
            "architecture_type": self.architecture_type,
            "stare_params": self.stare_params,
            "gcn_params": self.gcn_params,
            "transformer_params": self.transformer_params,
            "mlp_params": self.mlp_params,
        }

        self.separate_networks = separate_networks

        # Determine which policies need RL
        self.forget_needs_rl = forget_policy == "rl"
        self.remember_needs_rl = remember_policy == "rl"
        self.qa_needs_rl = qa_policy == "rl"
        self.explore_needs_rl = explore_policy == "rl"

        # Count how many policies need RL
        rl_policies = []
        if self.forget_needs_rl:
            rl_policies.append("forget")
        if self.remember_needs_rl:
            rl_policies.append("remember")
        if self.qa_needs_rl:
            rl_policies.append("qa")
        if self.explore_needs_rl:
            rl_policies.append("explore")

        # Validate separate_networks usage
        if self.separate_networks and len(rl_policies) < 2:
            raise ValueError(
                f"separate_networks=True requires at least 2 RL policies. "
                f"Got {len(rl_policies)} RL policies: {rl_policies}. "
                f"Use separate_networks=False when learning only one policy."
            )

        if self.separate_networks:
            # Create separate networks for each RL policy
            self.networks = {}
            self.target_networks = {}
            self.optimizers = {}

            for policy in rl_policies:
                # Each network is specialized for one policy only
                policy_gnn_params = gnn_params.copy()
                policy_gnn_params["separate_network_type"] = policy
                policy_gnn_params["forget_needs_rl"] = policy == "forget"
                policy_gnn_params["remember_needs_rl"] = policy == "remember"
                policy_gnn_params["qa_needs_rl"] = policy == "qa"
                policy_gnn_params["explore_needs_rl"] = policy == "explore"

                self.networks[policy] = GNN(**policy_gnn_params)
                
                # QA doesn't need target network (contextual bandit)
                if policy != "qa":
                    self.target_networks[policy] = GNN(**policy_gnn_params)
                    self.target_networks[policy].load_state_dict(
                        self.networks[policy].state_dict()
                    )
                    self.target_networks[policy].eval()

                    # Disable gradients for target network
                    for param in self.target_networks[policy].parameters():
                        param.requires_grad = False

                self.optimizers[policy] = optim.Adam(
                    list(self.networks[policy].parameters()), lr=self.learning_rate
                )

            # Set shared networks to None
            self.dqn = None
            self.dqn_target = None
            self.optimizer = None
        else:
            # Use shared network - all RL policies share the same backbone
            gnn_params["separate_network_type"] = None  # Shared network
            gnn_params["forget_needs_rl"] = self.forget_needs_rl
            gnn_params["remember_needs_rl"] = self.remember_needs_rl
            gnn_params["qa_needs_rl"] = self.qa_needs_rl
            gnn_params["explore_needs_rl"] = self.explore_needs_rl

            self.dqn = GNN(**gnn_params)
            
            # For shared networks, we still need target network even if QA is included
            # because other policies (remember, forget, explore) need it
            if any(policy == "rl" for policy in [forget_policy, remember_policy, explore_policy]):
                self.dqn_target = GNN(**gnn_params)
                self.dqn_target.load_state_dict(self.dqn.state_dict())
                self.dqn_target.eval()

                # Disable gradients for target network
                for param in self.dqn_target.parameters():
                    param.requires_grad = False
            else:
                # If only QA uses RL, no target network needed
                self.dqn_target = None

            # optimizer
            self.optimizer = optim.Adam(
                list(self.dqn.parameters()), lr=self.learning_rate
            )

            # Set separate networks to None
            self.networks = {}
            self.target_networks = {}
            self.optimizers = {}

        self.q_values = {
            "train": {"remember": [], "forget": [], "qa": [], "explore": []},
            "val": {"remember": [], "forget": [], "qa": [], "explore": []},
            "test": {"remember": [], "forget": [], "qa": [], "explore": []},
        }

        self._save_number_of_parameters()
        self.init_memory_systems()

    def _save_number_of_parameters(self) -> None:
        r"""Save the number of parameters in the model."""
        if self.separate_networks:
            dict_ = {"total": 0}

            for policy_name, network in self.networks.items():
                policy_params = self._count_network_parameters(network)
                dict_[f"{policy_name}_network"] = policy_params
                dict_["total"] += policy_params["total"]
        else:
            dict_ = self._count_network_parameters(self.dqn)

        write_yaml(dict_, os.path.join(self.default_root_dir, "num_params.yaml"))

    def _count_network_parameters(self, network):
        """Count parameters for a network, handling both GNN and Transformer architectures."""
        if network.architecture_type == "transformer":
            total_params = sum(p.numel() for p in network.parameters())

            params_dict = {
                "total": total_params,
                "architecture": "transformer",
            }

            transformer_model = network.transformer_model

            # Detailed breakdown of transformer tokenizer components
            tokenizer = transformer_model.tokenizer
            params_dict.update(
                {
                    "tokenizer_entity_embeddings": tokenizer.entity_embeddings.numel(),
                    "tokenizer_relation_embeddings": tokenizer.relation_embeddings.numel(),
                    "tokenizer_qualifier_mlp": sum(
                        p.numel() for p in tokenizer.qualifier_mlp.parameters()
                    ),
                    "tokenizer_qualifier_attention": sum(
                        p.numel() for p in tokenizer.qualifier_attention.parameters()
                    ),
                    "tokenizer_token_projection": sum(
                        p.numel() for p in tokenizer.token_projection.parameters()
                    ),
                }
            )

            # Transformer encoder
            params_dict["transformer_encoder"] = sum(
                p.numel() for p in transformer_model.transformer.parameters()
            )

            # Policy-specific components
            if hasattr(transformer_model, "attention_aggregator_forget"):
                params_dict["attention_aggregator_forget"] = sum(
                    p.numel()
                    for p in transformer_model.attention_aggregator_forget.parameters()
                )
            if hasattr(transformer_model, "mlp_forget"):
                params_dict["mlp_forget"] = sum(
                    p.numel() for p in transformer_model.mlp_forget.parameters()
                )
            if hasattr(transformer_model, "attention_aggregator_qa"):
                params_dict["attention_aggregator_qa"] = sum(
                    p.numel()
                    for p in transformer_model.attention_aggregator_qa.parameters()
                )
            if hasattr(transformer_model, "mlp_qa"):
                params_dict["mlp_qa"] = sum(
                    p.numel() for p in transformer_model.mlp_qa.parameters()
                )
            if hasattr(transformer_model, "attention_aggregator_explore"):
                params_dict["attention_aggregator_explore"] = sum(
                    p.numel()
                    for p in transformer_model.attention_aggregator_explore.parameters()
                )
            if hasattr(transformer_model, "mlp_explore"):
                params_dict["mlp_explore"] = sum(
                    p.numel() for p in transformer_model.mlp_explore.parameters()
                )
            if hasattr(transformer_model, "mlp_remember"):
                params_dict["mlp_remember"] = sum(
                    p.numel() for p in transformer_model.mlp_remember.parameters()
                )

            return params_dict
        else:
            params_dict = {
                "total": sum(p.numel() for p in network.parameters()),
                "architecture": network.architecture_type,
                "gcn_layers": sum(p.numel() for p in network.gcn_layers.parameters()),
                "entity_embeddings": network.entity_embeddings.numel(),
                "relation_embeddings": network.relation_embeddings.numel(),
            }

            if hasattr(network, "attention_aggregator_forget"):
                params_dict["attention_aggregator_forget"] = sum(
                    p.numel() for p in network.attention_aggregator_forget.parameters()
                )
            if hasattr(network, "mlp_forget"):
                params_dict["mlp_forget"] = sum(
                    p.numel() for p in network.mlp_forget.parameters()
                )
            if hasattr(network, "attention_aggregator_qa"):
                params_dict["attention_aggregator_qa"] = sum(
                    p.numel() for p in network.attention_aggregator_qa.parameters()
                )
            if hasattr(network, "mlp_qa"):
                params_dict["mlp_qa"] = sum(
                    p.numel() for p in network.mlp_qa.parameters()
                )
            if hasattr(network, "attention_aggregator_explore"):
                params_dict["attention_aggregator_explore"] = sum(
                    p.numel() for p in network.attention_aggregator_explore.parameters()
                )
            if hasattr(network, "mlp_explore"):
                params_dict["mlp_explore"] = sum(
                    p.numel() for p in network.mlp_explore.parameters()
                )
            if hasattr(network, "mlp_remember"):
                params_dict["mlp_remember"] = sum(
                    p.numel() for p in network.mlp_remember.parameters()
                )

            return params_dict

    def init_memory_systems(self) -> None:
        r"""Initialize the agent's memory systems. This has nothing to do with the
        replay buffer."""

        self.current_step = 0
        self.current_time = self.base_date + timedelta(days=self.current_step)
        self.humemai.reset()

        assert self.pretrain_semantic in [False, "exclude_walls", "include_walls"]
        if self.pretrain_semantic in ["exclude_walls", "include_walls"]:

            if self.pretrain_semantic == "exclude_walls":
                exclude_walls = True
            else:
                exclude_walls = False
            room_layout = self.env.unwrapped.return_room_layout(exclude_walls)

            for triple in room_layout:
                self.humemai.add_semantic_memory(
                    triples=[[URIRef(item) for item in triple]],
                    qualifiers={
                        self.humemai_ns.time_added: Literal(
                            self.current_time.isoformat(timespec="seconds"),
                            datatype=XSD.dateTime,
                        ),
                        self.humemai_ns.derived_from: Literal(
                            "user",
                            datatype=XSD.string,
                        ),
                    },
                )
                if (
                    self.humemai.get_long_term_memory_count()
                    >= self.max_long_term_memory_size
                ):
                    break

    def encode_all_observations(self) -> None:
        """Encode all observations into short-term memories."""

        assert isinstance(self.observations["room"], list), "`room` should be a list."

        memory_list = self.humemai.to_list()
        short = [mem for mem in memory_list if "current_time" in mem[-1].keys()]

        assert len(short) == 0, "Short-term memory should be empty."

        # Encode new observations as short-term memory
        triples = [[URIRef(item) for item in obs] for obs in self.observations["room"]]
        qualifiers = {
            self.humemai_ns.current_time: Literal(
                self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
            )
        }
        self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

    def reset(self) -> None:
        r"""Reset the agent's environment and memory systems."""
        self.init_memory_systems()
        self.observations, info = self.env.reset()

        # encode observations as short-term
        self.encode_all_observations()

    def step(self, greedy: bool) -> tuple[
        np.ndarray,
        np.ndarray,
        np.ndarray,
        np.ndarray,
        np.ndarray,
        np.ndarray,
        np.ndarray,
        np.ndarray,
        int,
        list[str],
        bool,
    ]:
        r"""Step of the algorithm. This is the only step that interacts with the
        environment.

        Args:
            greedy: whether to use greedy policy

        Returns:
            a_remember, q_remember, a_forget, q_forget, a_qa, q_qa, a_explore, q_explore, reward, answers, done

        """
        # 1. QA policy - answer questions
        answers = []
        a_qa = np.array([np.nan])
        q_qa = np.array([[np.nan] * len(self.qa2str)])

        if self.qa_policy in [
            "most_recently_added",
            "most_recently_used",
            "most_frequently_used",
        ]:
            # Use symbolic QA policy
            a_qa = np.array([self.qa2int[self.qa_policy]])
            for question in self.observations["questions"]:
                answer = self.answer_question(question)
                answers.append(str(answer))
        elif self.qa_policy == "rl":
            # Use RL QA policy
            memory_list = self.humemai.to_list()
            dqn_to_use = self._get_network_for_policy("qa")
            a_qa, q_qa = select_action(
                state=memory_list,
                greedy=greedy,
                dqn=dqn_to_use,
                epsilon=self.epsilon,
                policy_type="qa",
            )
            # Temporarily override qa_policy to use existing answer_question method
            original_qa_policy = self.qa_policy
            self.qa_policy = self.qa2str[a_qa.item()]
            for question in self.observations["questions"]:
                answer = self.answer_question(question)
                answers.append(str(answer))
            # Restore original policy
            self.qa_policy = original_qa_policy
        else:
            raise NotImplementedError(
                f"QA policy '{self.qa_policy}' is not implemented."
            )

        # 2. Explore policy - determine exploration direction
        a_explore = np.array([np.nan])
        q_explore = np.array([[np.nan] * len(self.explore2str)])

        if self.explore_policy in ["dijkstra", "bfs"]:
            # Use symbolic explore policy
            a_explore = np.array([self.explore2int[self.explore_policy]])
            explore_direction = self.explore()
        elif self.explore_policy == "rl":
            # Use RL explore policy
            memory_list = self.humemai.to_list()
            dqn_to_use = self._get_network_for_policy("explore")
            a_explore, q_explore = select_action(
                state=memory_list,
                greedy=greedy,
                dqn=dqn_to_use,
                epsilon=self.epsilon,
                policy_type="explore",
            )
            # Apply the selected exploration strategy
            explore_strategy = self.explore2str[a_explore.item()]
            if explore_strategy == "dijkstra":
                explore_direction = self._explore_dijkstra()
            elif explore_strategy == "bfs":
                explore_direction = self._explore_bfs()
            else:
                raise ValueError(f"Unknown explore strategy: {explore_strategy}")
        else:
            raise NotImplementedError(
                f"Explore policy '{self.explore_policy}' is not implemented."
            )

        # 3. Remember policy - manage short-term memory
        memory_list = self.humemai.to_list()
        short_list = [mem for mem in memory_list if "current_time" in mem[-1].keys()]
        assert len(short_list) > 0, "Short-term memory should not be empty."

        if self.remember_policy == "all":
            self.humemai.move_all_short_term_to_episodic()
            a_remember = np.array([self.remember2int["remember"]] * len(short_list))
            q_remember = np.array([[np.nan] * len(self.remember2str)] * len(short_list))

        elif self.remember_policy == "rl":
            dqn_to_use = self._get_network_for_policy("remember")
            a_remember, q_remember = select_action(
                state=memory_list,
                greedy=greedy,
                dqn=dqn_to_use,
                epsilon=self.epsilon,
                policy_type="remember",
            )

            assert len(a_remember) == len(
                short_list
            ), "The number of actions should be equal to the number of short-term memories."

            for a_remember_, mem_short in zip(a_remember, short_list):
                if a_remember_ == self.remember2int["remember"]:
                    self.humemai.move_short_term_to_episodic(
                        memory_id_to_move=Literal(mem_short[-1]["memory_id"])
                    )
                elif a_remember_ == self.remember2int["forget"]:
                    self.humemai.delete_memory(Literal(mem_short[-1]["memory_id"]))
                else:
                    raise ValueError(
                        f"Invalid action: {a_remember_}. "
                        "Use 'remember' or 'forget' to specify the action."
                    )

        else:
            raise NotImplementedError(
                f"Remember policy '{self.remember_policy}' is not implemented. "
                "Use 'all' or 'rl' to specify the policy."
            )

        # 4. Forget policy - manage long-term memory
        a_forget = np.array([np.nan])
        q_forget = np.array([[np.nan] * len(self.forget2str)])

        if self.humemai.get_long_term_memory_count() > self.max_long_term_memory_size:

            if self.forget_policy == "fifo":
                a_forget = np.array([self.forget2int["fifo"]])
                a_forget_str = "fifo"
            elif self.forget_policy == "lru":
                a_forget = np.array([self.forget2int["lru"]])
                a_forget_str = "lru"
            elif self.forget_policy == "lfu":
                a_forget = np.array([self.forget2int["lfu"]])
                a_forget_str = "lfu"
            elif self.forget_policy == "rl":
                memory_list = self.humemai.to_list()  # get updated memory list
                dqn_to_use = self._get_network_for_policy("forget")
                a_forget, q_forget = select_action(
                    state=memory_list,
                    greedy=greedy,
                    dqn=dqn_to_use,
                    epsilon=self.epsilon,
                    policy_type="forget",
                )
                a_forget_str = self.forget2str[a_forget.item()]  # one item
            else:
                raise NotImplementedError(
                    f"Forget policy '{self.forget_policy}' is not implemented. "
                    "Use 'fifo', 'lru', 'lfu', or 'rl' to specify the policy."
                )

            while (
                self.humemai.get_long_term_memory_count()
                > self.max_long_term_memory_size
            ):
                if a_forget_str == "fifo":
                    mem_id_to_delete = self._pick_fifo_victim()
                elif a_forget_str == "lru":
                    mem_id_to_delete = self._pick_lru_victim()
                elif a_forget_str == "lfu":
                    mem_id_to_delete = self._pick_lfu_victim()
                else:
                    raise ValueError(
                        f"Invalid action: {a_forget_str}. "
                        "Use 'fifo', 'lru', or 'lfu' to specify the action."
                    )

                if mem_id_to_delete is None:
                    raise ValueError("No memory ID found for deletion.")
                self.humemai.delete_memory(Literal(mem_id_to_delete))

        # 5. Interact with environment
        (
            self.observations,
            reward,
            done,
            truncated,
            info,
        ) = self.env.step((answers, explore_direction))
        done = done or truncated

        # update current time
        self.current_step += 1
        self.current_time = self.base_date + timedelta(days=self.current_step)

        # 6. encode_all_observations
        self.encode_all_observations()

        return (
            a_remember,
            q_remember,
            a_forget,
            q_forget,
            a_qa,
            q_qa,
            a_explore,
            q_explore,
            sum(reward),
            answers,
            done,
        )

    def fill_replay_buffer(self) -> None:
        r"""Make the replay buffer full in the beginning with the uniformly-sampled
        actions. The filling continues until it reaches the warm start size.

        """
        self.replay_buffer_remember = ReplayBuffer(
            self.replay_buffer_size, self.batch_size
        )
        self.replay_buffer_forget = ReplayBuffer(
            self.replay_buffer_size, self.batch_size
        )
        self.replay_buffer_qa = ReplayBuffer(self.replay_buffer_size, self.batch_size)
        self.replay_buffer_explore = ReplayBuffer(
            self.replay_buffer_size, self.batch_size
        )
        done = True

        while (
            len(self.replay_buffer_remember) < self.warm_start
            or len(self.replay_buffer_forget) < self.warm_start
            or len(self.replay_buffer_qa) < self.warm_start
            or len(self.replay_buffer_explore) < self.warm_start
        ):
            if done:
                self.reset()
                done = False
            else:
                state = deepcopy(self.humemai.to_list())
                (
                    a_remember,
                    q_remember,
                    a_forget,
                    q_forget,
                    a_qa,
                    q_qa,
                    a_explore,
                    q_explore,
                    reward,
                    answers,
                    done,
                ) = self.step(greedy=False)
                next_state = deepcopy(self.humemai.to_list())

                if not np.isnan(a_remember).any():
                    self.replay_buffer_remember.store(
                        *[
                            state,
                            a_remember,
                            reward,
                            next_state,
                            done,
                        ]
                    )

                if not np.isnan(a_forget).any():
                    self.replay_buffer_forget.store(
                        *[
                            state,
                            a_forget,
                            reward,
                            next_state,
                            done,
                        ]
                    )

                if not np.isnan(a_qa).any():
                    # For QA (contextual bandit), we don't need next_state or done
                    # Store None for these to maintain interface compatibility
                    self.replay_buffer_qa.store(
                        *[
                            state,
                            a_qa,
                            reward,
                            None,  # next_state not needed for contextual bandit
                            False,  # done not needed for contextual bandit
                        ]
                    )

                if not np.isnan(a_explore).any():
                    self.replay_buffer_explore.store(
                        *[
                            state,
                            a_explore,
                            reward,
                            next_state,
                            done,
                        ]
                    )

    def train(self) -> None:
        r"""Train the agent."""
        self.fill_replay_buffer()  # fill up the buffer till warm start size

        self.epsilons = []
        self.training_loss = {
            "total": [],
            "remember": [],
            "forget": [],
            "qa": [],
            "explore": [],
        }
        self.scores = {"train": [], "val": [], "test": None}

        if self.separate_networks:
            for network in self.networks.values():
                network.train()
        else:
            self.dqn.train()

        done = True
        score = 0
        self.iteration_idx = 0

        while True:
            if done:
                self.reset()
                done = False
            else:
                state = deepcopy(self.humemai.to_list())
                (
                    a_remember,
                    q_remember,
                    a_forget,
                    q_forget,
                    a_qa,
                    q_qa,
                    a_explore,
                    q_explore,
                    reward,
                    answers,
                    done,
                ) = self.step(greedy=False)
                score += reward
                next_state = deepcopy(self.humemai.to_list())

                if not np.isnan(a_remember).any():
                    self.replay_buffer_remember.store(
                        *[
                            state,
                            a_remember,
                            reward,
                            next_state,
                            done,
                        ]
                    )

                if not np.isnan(a_forget).any():
                    self.replay_buffer_forget.store(
                        *[
                            state,
                            a_forget,
                            reward,
                            next_state,
                            done,
                        ]
                    )

                if not np.isnan(a_qa).any():
                    # For QA (contextual bandit), we don't need next_state or done
                    self.replay_buffer_qa.store(
                        *[
                            state,
                            a_qa,
                            reward,
                            None,  # next_state not needed for contextual bandit
                            False,  # done not needed for contextual bandit
                        ]
                    )

                if not np.isnan(a_explore).any():
                    self.replay_buffer_explore.store(
                        *[
                            state,
                            a_explore,
                            reward,
                            next_state,
                            done,
                        ]
                    )

                self.q_values["train"]["forget"].append(q_forget)
                self.q_values["train"]["remember"].append(q_remember)
                self.q_values["train"]["qa"].append(q_qa)
                self.q_values["train"]["explore"].append(q_explore)
                self.iteration_idx += 1

            if done:
                self.scores["train"].append(score)
                score = 0

                if (
                    self.iteration_idx
                    % (
                        self.validation_interval
                        * (self.env_config["terminates_at"] + 1)
                    )
                    == 0
                ):
                    with torch.no_grad():
                        self.validate()

            else:
                loss_remember, loss_forget, loss_qa, loss_explore, loss = update_model(
                    forget_policy=self.forget_policy,
                    remember_policy=self.remember_policy,
                    qa_policy=self.qa_policy,
                    explore_policy=self.explore_policy,
                    replay_buffer_remember=self.replay_buffer_remember,
                    replay_buffer_forget=self.replay_buffer_forget,
                    replay_buffer_qa=self.replay_buffer_qa,
                    replay_buffer_explore=self.replay_buffer_explore,
                    optimizer=self.optimizer if not self.separate_networks else None,
                    optimizers=self.optimizers if self.separate_networks else None,
                    device=self.device,
                    dqn=self.dqn if not self.separate_networks else None,
                    dqn_target=self.dqn_target if not self.separate_networks else None,
                    networks=self.networks if self.separate_networks else None,
                    target_networks=(
                        self.target_networks if self.separate_networks else None
                    ),
                    ddqn=self.ddqn,
                    gamma=self.gamma,
                    use_gradient_clipping=self.use_gradient_clipping,
                    gradient_clip_value=self.gradient_clip_value,
                    separate_networks=self.separate_networks,
                )

                self.training_loss["total"].append(loss)
                self.training_loss["remember"].append(loss_remember)
                self.training_loss["forget"].append(loss_forget)
                self.training_loss["qa"].append(loss_qa)
                self.training_loss["explore"].append(loss_explore)

                # linearly decay epsilon
                self.epsilon = update_epsilon(
                    self.epsilon,
                    self.max_epsilon,
                    self.min_epsilon,
                    self.epsilon_decay_until,
                )
                self.epsilons.append(self.epsilon)

                # For QA (contextual bandit), we don't need target network updates
                # since there's no temporal difference learning involved
                if self.iteration_idx % self.target_update_interval == 0:
                    if self.separate_networks:
                        for policy_type in self.networks:
                            if policy_type != "qa":  # Skip QA for target updates
                                target_hard_update(
                                    dqn=self.networks[policy_type],
                                    dqn_target=self.target_networks[policy_type],
                                )
                    else:
                        # Only update if target network exists (i.e., non-QA-only scenarios)
                        if self.dqn_target is not None:
                            target_hard_update(dqn=self.dqn, dqn_target=self.dqn_target)

                # plotting & show training results
                if (
                    self.iteration_idx == self.num_iterations
                    or self.iteration_idx % self.plotting_interval == 0
                ):
                    self.plot_results("all", save_fig=True)

                if self.iteration_idx >= self.num_iterations:
                    break

        with torch.no_grad():
            self.test()

        self.env.close()

    def validate_test_middle(self, val_or_test: str) -> tuple[list, list, list, list]:
        r"""A function shared by validation and test in the middle.

        Args:
            val_or_test: "val" or "test"

        Returns:
            scores_local: a list of total episode rewards
            states_local: memory states
            q_values_local: q values
            actions_local: greey actions taken

        """
        scores_local = []
        states_local = []
        q_values_local = []
        actions_local = []

        for idx in range(self.num_samples_for_results[val_or_test]):
            done = True
            score = 0
            while True:
                if done:
                    self.reset()
                    done = False

                else:
                    state = deepcopy(self.humemai.to_list())
                    (
                        a_remember,
                        q_remember,
                        a_forget,
                        q_forget,
                        a_qa,
                        q_qa,
                        a_explore,
                        q_explore,
                        reward,
                        answers,
                        done,
                    ) = self.step(greedy=True)

                    score += reward

                    if idx == self.num_samples_for_results[val_or_test] - 1:
                        states_local.append(state)
                        q_values_local.append(
                            {
                                "forget": q_forget,
                                "remember": q_remember,
                                "qa": q_qa,
                                "explore": q_explore,
                            }
                        )
                        actions_local.append(
                            {
                                "forget": a_forget,
                                "remember": a_remember,
                                "qa": a_qa,
                                "explore": a_explore,
                            }
                        )
                        self.q_values[val_or_test]["forget"].append(q_forget)
                        self.q_values[val_or_test]["remember"].append(q_remember)
                        self.q_values[val_or_test]["qa"].append(q_qa)
                        self.q_values[val_or_test]["explore"].append(q_explore)

                if done:
                    break

            scores_local.append(score)

        return scores_local, states_local, q_values_local, actions_local

    def validate(self) -> None:
        r"""Validate the agent."""
        if self.separate_networks:
            for network in self.networks.values():
                network.eval()
        else:
            self.dqn.eval()

        scores_temp, states, q_values, actions = self.validate_test_middle("val")

        num_episodes = self.iteration_idx // (self.env_config["terminates_at"] + 1) - 1

        # Save validation checkpoints based on network configuration
        if self.separate_networks:
            self._save_separate_networks_validation(scores_temp, num_episodes)
        else:
            save_validation(
                scores_temp=scores_temp,
                scores=self.scores,
                default_root_dir=self.default_root_dir,
                num_episodes=num_episodes,
                validation_interval=self.validation_interval,
                val_file_names=self.val_file_names,
                dqn=self.dqn,
            )

        save_states_q_values_actions(
            states, q_values, actions, self.default_root_dir, "val", num_episodes
        )
        self.env.close()

        if self.separate_networks:
            for network in self.networks.values():
                network.train()
        else:
            self.dqn.train()

    def _save_separate_networks_validation(
        self, scores_temp: list, num_episodes: int
    ) -> None:
        """Save validation checkpoints for separate networks."""
        mean_score = round(np.mean(scores_temp).item())

        # Create checkpoint dictionary for all separate networks
        checkpoint = {}
        for policy_name, network in self.networks.items():
            checkpoint[f"{policy_name}_network"] = network.state_dict()

        filename = os.path.join(
            self.default_root_dir, f"episode={num_episodes}_val-score={mean_score}.pt"
        )
        torch.save(checkpoint, filename)
        self.val_file_names.append(filename)

        # Update validation scores
        for _ in range(self.validation_interval):
            self.scores["val"].append(scores_temp)

        # Keep only the best validation checkpoint
        scores_to_compare = []
        for fn in self.val_file_names:
            score = int(fn.split("val-score=")[-1].split(".pt")[0])
            scores_to_compare.append(score)

        from .utils import list_duplicates_of

        indexes = list_duplicates_of(scores_to_compare, max(scores_to_compare))
        file_to_keep = self.val_file_names[indexes[-1]]

        for fn in self.val_file_names:
            if fn != file_to_keep:
                os.remove(fn)
                self.val_file_names.remove(fn)

    def test(self, checkpoint: str | None = None) -> None:
        r"""Test the agent."""
        if self.separate_networks:
            for network in self.networks.values():
                network.eval()
        else:
            self.dqn.eval()

        self.env_config["seed"] = self.test_seed
        self.env = gym.make(self.env_str, **self.env_config)

        assert len(self.val_file_names) == 1, f"{len(self.val_file_names)} should be 1"

        # Load the best validation checkpoint
        if self.separate_networks:
            self._load_separate_networks_checkpoint(checkpoint)
        else:
            self.dqn.load_state_dict(torch.load(self.val_file_names[0]))
            if checkpoint is not None:
                self.dqn.load_state_dict(torch.load(checkpoint))

        scores, states, q_values, actions = self.validate_test_middle("test")
        self.scores["test"] = scores

        save_final_results(
            self.scores,
            self.training_loss,
            self.default_root_dir,
            self.q_values,
            self,
        )
        save_states_q_values_actions(
            states, q_values, actions, self.default_root_dir, "test"
        )

        self.plot_results("all", save_fig=True)
        self.env.close()

        if self.separate_networks:
            for network in self.networks.values():
                network.train()
        else:
            self.dqn.train()

    def _load_separate_networks_checkpoint(self, checkpoint: str | None = None) -> None:
        """Load checkpoints for separate networks."""
        if checkpoint is not None:
            # Load custom checkpoint
            checkpoint_dict = torch.load(checkpoint)
        else:
            # Load validation checkpoint
            checkpoint_dict = torch.load(self.val_file_names[0])

        # Load state dicts for available networks
        for policy_name, network in self.networks.items():
            checkpoint_key = f"{policy_name}_network"
            if checkpoint_key in checkpoint_dict:
                network.load_state_dict(checkpoint_dict[checkpoint_key])

    def _get_network_for_policy(self, policy_type: str) -> torch.nn.Module:
        """Get the appropriate network for a given policy type.

        Args:
            policy_type: The policy type ("remember", "forget", "qa", "explore")

        Returns:
            The network to use for the given policy type
        """
        if self.separate_networks:
            if policy_type not in self.networks:
                raise ValueError(f"No network found for policy type: {policy_type}")
            return self.networks[policy_type]
        else:
            return self.dqn

    def plot_results(self, to_plot: str = "all", save_fig: bool = False) -> None:
        r"""Plot things for DQN training.

        Args:
            to_plot: what to plot:
                training_td_loss
                epsilons
                training_score
                validation_score
                test_score
                q_values_train
                q_values_val
                q_values_test

        """
        plot_results(
            self.scores,
            self.training_loss,
            self.epsilons,
            self.q_values,
            self.iteration_idx,
            self.num_iterations,
            self.env.unwrapped.total_maximum_episode_rewards,
            self.default_root_dir,
            self.remember2str,
            self.forget2str,
            self.qa2str,
            self.explore2str,
            to_plot,
            save_fig,
        )
