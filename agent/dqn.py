from copy import deepcopy
from typing import Any
import os
from datetime import timedelta
import torch
import torch.optim as optim
from rdflib import XSD, Literal, URIRef

from .long import LongTermAgent
from .nn import GNN
from .utils import write_yaml, select_action


class DQNAgent(LongTermAgent):
    """
    DQNAgent is a specialized LongTermAgent that uses Deep Q-Learning for decision making.
    It inherits from LongTermAgent and implements the DQN algorithm.
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
        qa_policy: str = "most_frequently_used",
        explore_policy: str = "dijkstra",
        mm_long_policy: str = "lfu",
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
        rl_state: str = "all",
    ) -> None:
        r"""Initialize the DQNAgent.
        Args:
            env_str: The name of the environment to use.
            env_config: A dictionary containing the environment configuration.
            qa_policy: The policy to use for answering questions.
            explore_policy: The policy to use for exploration.
            mm_long_policy: The policy to use for long-term memory management.
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
            rl_state: The state representation to use for reinforcement learning
                ("all", "short"). Default is "all", which uses both short-term and
                long-term memories.

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
        self.rl_state = rl_state

        assert self.batch_size <= self.warm_start <= self.replay_buffer_size

        self.action2str = {0: "remember", 1: "forget"}
        self.action2int = {v: k for k, v in self.action2str.items()}

        self.dqn_params["device"] = self.device
        self.dqn_params["entities"] = [
            e for entities in self.env.unwrapped.entities.values() for e in entities
        ]  # main entities
        self.dqn_params["entities"] += [
            str(i) for i in range(1000)
        ]  # number entities for `num_recalled`

        # Add date strings from base_date + 0 to 100 days
        self.dqn_params["entities"] += [
            (self.base_date + timedelta(days=i)).isoformat(timespec="seconds")
            for i in range(101)  # 0 to 100 inclusive
        ]  # date entities for temporal reasoning

        # Main triple relations have "inv", while qualifier relations don't have "inv".
        self.dqn_params["relations"] = (
            self.env.unwrapped.relations
            + [rel + "_inv" for rel in self.env.unwrapped.relations]
            + ["current_time", "time_added", "last_accessed", "num_recalled"]
        )

        self.dqn = GNN(**self.dqn_params)
        self.dqn_target = GNN(**self.dqn_params)
        self.dqn_target.load_state_dict(self.dqn.state_dict())
        self.dqn_target.eval()

        # optimizer
        self.optimizer = optim.Adam(list(self.dqn.parameters()), lr=self.learning_rate)

        self.q_values = {"train": [], "val": [], "test": []}

        self._save_number_of_parameters()

    def _save_number_of_parameters(self) -> None:
        r"""Save the number of parameters in the model."""
        write_yaml(
            {
                "total": sum(p.numel() for p in self.dqn.parameters()),
                "gcn_layers": sum(p.numel() for p in self.dqn.gcn_layers.parameters()),
                "mlp": sum(p.numel() for p in self.dqn.mlp.parameters()),
                "entity_embeddings": self.dqn.entity_embeddings.numel(),
                "relation_embeddings": self.dqn.relation_embeddings.numel(),
            },
            os.path.join(self.default_root_dir, "num_params.yaml"),
        )

    def get_memory_list(self) -> list[list[str]]:
        """Get a list of all memory entities.

        Returns:
            List of all memories.
        """
        memory_list = self.humemai.to_list()

        short = [mem for mem in memory_list if "current_time" in mem[-1].keys()]

        long = [mem for mem in memory_list if "current_time" not in mem[-1].keys()]

        return {
            "all": memory_list,
            "short": short,
            "long": long,
        }

    def encode_all_observations(self) -> None:
        """Encode all observations into short-term memories."""

        assert isinstance(self.observations["room"], list), "`room` should be a list."
        memory_list = self.get_memory_list()
        assert len(memory_list["short"]) == 0, "Short-term memory should be empty."

        # insert new observations in short-term
        self.current_time = self.base_date + timedelta(days=self.current_step)
        triples = [[URIRef(item) for item in obs] for obs in self.observations["room"]]
        qualifiers = {
            self.humemai_ns.current_time: Literal(
                self.current_time.isoformat(timespec="seconds"), datatype=XSD.dateTime
            )
        }
        self.humemai.add_short_term_memory(triples=triples, qualifiers=qualifiers)

    def reset(self) -> None:
        self.current_step = 0
        self.humemai.reset()
        self.observations, info = self.env.reset()

        # encode observations as short-term
        self.encode_all_observations()

    def step(self, greedy: bool) -> tuple[
        dict,
        list[int],
        list[list[float]],
        list[int],
        list[list[float]],
        float,
        float,
        list[str],
        bool,
    ]:
        r"""Step of the algorithm. This is the only step that interacts with the
        environment.

        Args:
            greedy: whether to use greedy policy

        Returns:
            action, q_value, reward, answers, done, explore

        """
        memory_list = self.get_memory_list()

        assert len(memory_list["short"]) > 0, "Short-term memory should not be empty."

        if self.rl_state == "short":
            state = memory_list["short"]
        elif self.rl_state == "all":
            state = memory_list["all"]
        else:
            raise ValueError(
                f"Invalid rl_state: {self.rl_state}. "
                "Use 'short' or 'all' to specify the state representation."
            )

        actions, q_values = select_action(
            state=state,
            greedy=greedy,
            dqn=self.dqn,
            epsilon=self.epsilon,
        )

        assert len(actions) == len(
            memory_list["short"]
        ), "The number of actions should be equal to the number of short-term memories."

        for action, mem_short in zip(actions, memory_list["short"]):

            if action == self.action2int["remember"]:
                self.humemai.move_short_term_to_episodic(
                    memory_id_to_move=mem_short[-1]["memoryID"]
                )



            manage_memory(self.memory_systems, self.action_mm2str[a_mm_], mem_short)

        (
            self.observations,
            reward,
            done,
            truncated,
            info,
        ) = self.env.step((answers, self.action_explore2str[a_explore.item()]))
        self.memory_systems.long.decay()
        self.num_semantic_decayed += 1
        done = done or truncated

        # 4. encode observations
        encode_all_observations(self.memory_systems, self.observations["room"])

        return (
            a_explore,
            q_explore,
            a_mm,
            q_mm,
            reward,
            intrinsic_explore_reward,
            answers,
            done,
        )
