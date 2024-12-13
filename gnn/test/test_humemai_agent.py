import logging

logger = logging.getLogger()
logger.disabled = True

import random
import unittest

from tqdm.auto import tqdm

from agent import DQNAgent


class DQNAgentTest(unittest.TestCase):
    def test_all_agents(self) -> None:
        terminates_at = 4
        batch_size = 2
        num_iterations = (terminates_at + 1) * 1
        for explore_policy in ["rl", "avoid_walls"]:
            for mm_policy in ["rl", "handcrafted"]:
                for capacity_long in [3]:
                    for pretrain_semantic in [
                        False,
                        "include_walls",
                        "exclude_walls",
                    ]:
                        for semantic_decay_factor in [0.8]:
                            for scale_reward in [True, False]:
                                params_dict = {
                                    "env_str": "room_env:RoomEnv-v2",
                                    "num_iterations": num_iterations,
                                    "replay_buffer_size": num_iterations,
                                    "warm_start": batch_size,
                                    "batch_size": batch_size,
                                    "target_update_interval": 1,
                                    "epsilon_decay_until": num_iterations,
                                    "max_epsilon": 1.0,
                                    "min_epsilon": 0.01,
                                    "gamma": {"mm": 0.9, "explore": 0.9},
                                    "learning_rate": 0.001,
                                    "capacity": {"long": capacity_long, "short": 15},
                                    "pretrain_semantic": pretrain_semantic,
                                    "semantic_decay_factor": semantic_decay_factor,
                                    "dqn_params": {
                                        "gcn_layer_params": {
                                            "type": "stare",
                                            "embedding_dim": 2,
                                            "num_layers": 2,
                                            "gcn_drop": 0.1,
                                            "triple_qual_weight": 0.8,
                                        },
                                        "relu_between_gcn_layers": True,
                                        "dropout_between_gcn_layers": True,
                                        "mlp_params": {
                                            "num_hidden_layers": 2,
                                            "dueling_dqn": True,
                                        },
                                    },
                                    "num_samples_for_results": {"val": 1, "test": 1},
                                    "validation_interval": 1,
                                    "plotting_interval": 50,
                                    "train_seed": 5,
                                    "test_seed": 0,
                                    "device": "cpu",
                                    "qa_function": "latest_strongest",
                                    "env_config": {
                                        "question_prob": 1.0,
                                        "terminates_at": terminates_at,
                                        "randomize_observations": "all",
                                        "room_size": "xl-different-prob",
                                        "rewards": {
                                            "correct": 1,
                                            "wrong": 0,
                                            "partial": 0,
                                        },
                                        "make_everything_static": False,
                                        "num_total_questions": 5,
                                        "question_interval": 1,
                                        "include_walls_in_observations": True,
                                    },
                                    "intrinsic_explore_reward": 0.5,
                                    "ddqn": True,
                                    "default_root_dir": "training-results/TRASH",
                                    "explore_policy": explore_policy,
                                    "mm_policy": mm_policy,
                                    "scale_reward": scale_reward,
                                }

                                agent = DQNAgent(**params_dict)
                                agent.train()

                                self.assertEqual(
                                    agent.num_semantic_decayed,
                                    terminates_at + 1,
                                )

                                agent.remove_results_from_disk()
