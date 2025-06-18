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
from .utils import (
    ReplayBuffer,
    plot_results,
    save_final_results,
    save_states_q_values_actions,
    save_validation,
    select_action,
    target_hard_update,
    update_epsilon,
    update_model,
    write_yaml,
)


class DQNAgent(LongTermAgent):
    """
    DQNAgent is a specialized LongTermAgent that uses Deep Q-Learning for decision
    making. It inherits from LongTermAgent and implements the DQN algorithm.
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
        dqn_params: dict = {
            "gcn_layer_params": {
                "type": "stare",
                "embedding_dim": 64,
                "num_layers": 2,
                "gcn_drop": 0.1,
                "triple_qual_weight": 0.8,
            },
            "relu_between_gcn_layers": True,
            "dropout_between_gcn_layers": True,
            "mlp_params": {"num_hidden_layers": 2, "dueling_dqn": True},
        },
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
            dqn_params: A dictionary containing the parameters for the DQN model.
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
        self.dqn_params = dqn_params
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
        self.forget2int = {v: k for k, v in self.forget2str.items()}
        self.remember2int = {v: k for k, v in self.remember2str.items()}

        self.dqn_params["device"] = self.device
        self.dqn_params["entities"] = [
            e for entities in self.env.unwrapped.entities.values() for e in entities
        ]  # main entities
        self.dqn_params["entities"] += ["user"]  # add user entity
        self.dqn_params["entities"] += [
            str(i) for i in range(env_config["terminates_at"] * 2)
        ]  # number entities for `num_recalled`

        # Add date strings
        self.dqn_params["entities"] += [
            (self.base_date + timedelta(days=i)).isoformat(timespec="seconds")
            for i in range(env_config["terminates_at"] + 2)
        ]  # date entities for temporal reasoning

        # Main triple relations have "inv", while qualifier relations don't have "inv".
        self.dqn_params["relations"] = (
            self.env.unwrapped.relations
            + [rel + "_inv" for rel in self.env.unwrapped.relations]
            + [
                "current_time",
                "time_added",
                "last_accessed",
                "num_recalled",
                "derived_from",
            ]
        )

        self.separate_networks = separate_networks

        # Determine which policies need RL
        self.forget_needs_rl = forget_policy == "rl"
        self.remember_needs_rl = remember_policy == "rl"

        # Validate separate_networks usage
        if self.separate_networks and not (self.forget_needs_rl and self.remember_needs_rl):
            raise ValueError(
                "separate_networks=True only makes sense when both forget_policy='rl' "
                f"and remember_policy='rl'. Got forget_policy='{forget_policy}' and "
                f"remember_policy='{remember_policy}'"
            )

        if self.separate_networks and (self.forget_needs_rl and self.remember_needs_rl):
            # Create separate networks for forget and remember policies
            self.dqn_forget = GNN(separate_network_type="forget", **self.dqn_params)
            self.dqn_target_forget = GNN(
                separate_network_type="forget", **self.dqn_params
            )
            self.dqn_target_forget.load_state_dict(self.dqn_forget.state_dict())
            self.dqn_target_forget.eval()
            self.optimizer_forget = optim.Adam(
                list(self.dqn_forget.parameters()), lr=self.learning_rate
            )

            self.dqn_remember = GNN(
                separate_network_type="remember", **self.dqn_params
            )
            self.dqn_target_remember = GNN(
                separate_network_type="remember", **self.dqn_params
            )
            self.dqn_target_remember.load_state_dict(self.dqn_remember.state_dict())
            self.dqn_target_remember.eval()
            self.optimizer_remember = optim.Adam(
                list(self.dqn_remember.parameters()), lr=self.learning_rate
            )

            # Set shared networks to None
            self.dqn = None
            self.dqn_target = None
            self.optimizer = None
        else:
            # Use shared network (existing behavior)
            self.dqn_params["forget_needs_rl"] = self.forget_needs_rl
            self.dqn_params["remember_needs_rl"] = self.remember_needs_rl

            self.dqn = GNN(**self.dqn_params)
            self.dqn_target = GNN(**self.dqn_params)
            self.dqn_target.load_state_dict(self.dqn.state_dict())
            self.dqn_target.eval()

            # optimizer
            self.optimizer = optim.Adam(
                list(self.dqn.parameters()), lr=self.learning_rate
            )

            # Set separate networks to None
            self.dqn_forget = None
            self.dqn_target_forget = None
            self.optimizer_forget = None
            self.dqn_remember = None
            self.dqn_target_remember = None
            self.optimizer_remember = None

        self.q_values = {
            "train": {"remember": [], "forget": []},
            "val": {"remember": [], "forget": []},
            "test": {"remember": [], "forget": []},
        }

        self._save_number_of_parameters()
        self.init_memory_systems()

    def _save_number_of_parameters(self) -> None:
        r"""Save the number of parameters in the model."""
        if self.separate_networks:
            dict_ = {"total": 0}
            
            if self.dqn_forget is not None:
                forget_params = {
                    "total": sum(p.numel() for p in self.dqn_forget.parameters()),
                    "gcn_layers": sum(p.numel() for p in self.dqn_forget.gcn_layers.parameters()),
                    "entity_embeddings": self.dqn_forget.entity_embeddings.numel(),
                    "relation_embeddings": self.dqn_forget.relation_embeddings.numel(),
                }
                if hasattr(self.dqn_forget, 'attention_aggregator_forget'):
                    forget_params["attention_aggregator_forget"] = sum(
                        p.numel() for p in self.dqn_forget.attention_aggregator_forget.parameters()
                    )
                if hasattr(self.dqn_forget, 'mlp_forget'):
                    forget_params["mlp_forget"] = sum(
                        p.numel() for p in self.dqn_forget.mlp_forget.parameters()
                    )
                
                dict_["dqn_forget"] = forget_params
                dict_["total"] += forget_params["total"]
            
            if self.dqn_remember is not None:
                remember_params = {
                    "total": sum(p.numel() for p in self.dqn_remember.parameters()),
                    "gcn_layers": sum(p.numel() for p in self.dqn_remember.gcn_layers.parameters()),
                    "entity_embeddings": self.dqn_remember.entity_embeddings.numel(),
                    "relation_embeddings": self.dqn_remember.relation_embeddings.numel(),
                }
                if hasattr(self.dqn_remember, 'mlp_remember'):
                    remember_params["mlp_remember"] = sum(
                        p.numel() for p in self.dqn_remember.mlp_remember.parameters()
                    )
                
                dict_["dqn_remember"] = remember_params
                dict_["total"] += remember_params["total"]
        else:
            dict_ = {
                "total": sum(p.numel() for p in self.dqn.parameters()),
                "gcn_layers": sum(p.numel() for p in self.dqn.gcn_layers.parameters()),
                "entity_embeddings": self.dqn.entity_embeddings.numel(),
                "relation_embeddings": self.dqn.relation_embeddings.numel(),
            }
            if hasattr(self.dqn, "attention_aggregator_forget"):
                dict_["attention_aggregator_forget"] = sum(
                    p.numel() for p in self.dqn.attention_aggregator_forget.parameters()
                )
            if hasattr(self.dqn, "mlp_remember"):
                dict_["mlp_remember"] = sum(
                    p.numel() for p in self.dqn.mlp_remember.parameters()
                )
            if hasattr(self.dqn, "mlp_forget"):
                dict_["mlp_forget"] = sum(
                    p.numel() for p in self.dqn.mlp_forget.parameters()
                )
        write_yaml(dict_, os.path.join(self.default_root_dir, "num_params.yaml"))

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

    def step(
        self, greedy: bool
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, list[str], bool]:
        r"""Step of the algorithm. This is the only step that interacts with the
        environment.

        Args:
            greedy: whether to use greedy policy

        Returns:
            a_remember, q_remember, a_forget, q_forget, reward, answers, done

        """
        # 1. generate answers and exploration direction
        answers, explore_direction = self._generate_action_pair(self.observations)

        # 2-a. manage short-term memory (remember policy)
        memory_list = self.humemai.to_list()
        short_list = [mem for mem in memory_list if "current_time" in mem[-1].keys()]
        assert len(short_list) > 0, "Short-term memory should not be empty."

        if self.remember_policy == "all":
            self.humemai.move_all_short_term_to_episodic()
            a_remember = np.array([self.remember2int["remember"]] * len(short_list))
            q_remember = np.array([[np.nan] * len(self.remember2str)] * len(short_list))

        elif self.remember_policy == "rl":
            if self.separate_networks:
                dqn_to_use = self.dqn_remember
            else:
                dqn_to_use = self.dqn

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

        # 2-b. manage long-term memory (forget policy)
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

                if self.separate_networks:
                    dqn_to_use = self.dqn_forget
                else:
                    dqn_to_use = self.dqn

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

        # 3. encode_all_observations
        self.encode_all_observations()

        return a_remember, q_remember, a_forget, q_forget, sum(reward), answers, done

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
        done = True

        while (
            len(self.replay_buffer_remember) < self.warm_start
            or len(self.replay_buffer_forget) < self.warm_start
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

    def train(self) -> None:
        r"""Train the agent."""
        self.fill_replay_buffer()  # fill up the buffer till warm start size

        self.epsilons = []
        self.training_loss = {"total": [], "remember": [], "forget": []}
        self.scores = {"train": [], "val": [], "test": None}

        if self.separate_networks:
            if self.dqn_forget is not None:
                self.dqn_forget.train()
            if self.dqn_remember is not None:
                self.dqn_remember.train()
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

                self.q_values["train"]["forget"].append(q_forget)
                self.q_values["train"]["remember"].append(q_remember)
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
                loss_remember, loss_forget, loss = update_model(
                    forget_policy=self.forget_policy,
                    remember_policy=self.remember_policy,
                    replay_buffer_remember=self.replay_buffer_remember,
                    replay_buffer_forget=self.replay_buffer_forget,
                    optimizer=self.optimizer if not self.separate_networks else None,
                    optimizer_forget=(
                        self.optimizer_forget if self.separate_networks else None
                    ),
                    optimizer_remember=(
                        self.optimizer_remember if self.separate_networks else None
                    ),
                    device=self.device,
                    dqn=self.dqn if not self.separate_networks else None,
                    dqn_target=self.dqn_target if not self.separate_networks else None,
                    dqn_forget=self.dqn_forget if self.separate_networks else None,
                    dqn_target_forget=(
                        self.dqn_target_forget if self.separate_networks else None
                    ),
                    dqn_remember=self.dqn_remember if self.separate_networks else None,
                    dqn_target_remember=(
                        self.dqn_target_remember if self.separate_networks else None
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

                # linearly decay epsilon
                self.epsilon = update_epsilon(
                    self.epsilon,
                    self.max_epsilon,
                    self.min_epsilon,
                    self.epsilon_decay_until,
                )
                self.epsilons.append(self.epsilon)

                # if hard update is needed
                if self.iteration_idx % self.target_update_interval == 0:
                    if self.separate_networks:
                        if self.dqn_forget is not None:
                            target_hard_update(
                                dqn=self.dqn_forget, dqn_target=self.dqn_target_forget
                            )
                        if self.dqn_remember is not None:
                            target_hard_update(
                                dqn=self.dqn_remember,
                                dqn_target=self.dqn_target_remember,
                            )
                    else:
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
                        reward,
                        answers,
                        done,
                    ) = self.step(greedy=True)

                    score += reward

                    if idx == self.num_samples_for_results[val_or_test] - 1:
                        states_local.append(state)
                        q_values_local.append(
                            {"forget": q_forget, "remember": q_remember}
                        )
                        actions_local.append(
                            {"forget": a_forget, "remember": a_remember}
                        )
                        self.q_values[val_or_test]["forget"].append(q_forget)
                        self.q_values[val_or_test]["remember"].append(q_remember)

                if done:
                    break

            scores_local.append(score)

        return scores_local, states_local, q_values_local, actions_local

    def validate(self) -> None:
        r"""Validate the agent."""
        if self.separate_networks:
            if self.dqn_forget is not None:
                self.dqn_forget.eval()
            if self.dqn_remember is not None:
                self.dqn_remember.eval()
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
            if self.dqn_forget is not None:
                self.dqn_forget.train()
            if self.dqn_remember is not None:
                self.dqn_remember.train()
        else:
            self.dqn.train()

    def _save_separate_networks_validation(self, scores_temp: list, num_episodes: int) -> None:
        """Save validation checkpoints for separate networks."""
        mean_score = round(np.mean(scores_temp).item())
        
        # Create checkpoint dictionary
        checkpoint = {}
        if self.dqn_forget is not None:
            checkpoint['dqn_forget'] = self.dqn_forget.state_dict()
        if self.dqn_remember is not None:
            checkpoint['dqn_remember'] = self.dqn_remember.state_dict()
        
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
        r"""Test the agent.

        Args:
            checkpoint: The checkpoint to override.

        """
        if self.separate_networks:
            if self.dqn_forget is not None:
                self.dqn_forget.eval()
            if self.dqn_remember is not None:
                self.dqn_remember.eval()
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
            if self.dqn_forget is not None:
                self.dqn_forget.train()
            if self.dqn_remember is not None:
                self.dqn_remember.train()
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
        if self.dqn_forget is not None and 'dqn_forget' in checkpoint_dict:
            self.dqn_forget.load_state_dict(checkpoint_dict['dqn_forget'])
        
        if self.dqn_remember is not None and 'dqn_remember' in checkpoint_dict:
            self.dqn_remember.load_state_dict(checkpoint_dict['dqn_remember'])

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
            to_plot,
            save_fig,
        )
