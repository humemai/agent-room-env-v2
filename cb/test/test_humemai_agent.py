import logging

logger = logging.getLogger()
logger.disabled = True

import random
import unittest

from tqdm.auto import tqdm

from agent import DQNAgent


class DQNAgentTest(unittest.TestCase):
    def test_all_agents(self) -> None:
        terminates_at = 99
        batch_size = 2
        num_iterations = (terminates_at + 1) * 1
        capacity_max = 12

        pretrained_path = "trained-results/non-equal-object-probs/dqn/room_size=xl-different-prob/capacity=12/2024-08-11 16:24:54.492650/"

        for use_raw_embeddings_for_qa in [False, True]:
            for qa_entities in ["all", "room"]:
                params_dict = {
                    "env_str": "room_env:RoomEnv-v2",
                    "num_iterations": num_iterations,
                    "replay_buffer_size": num_iterations,
                    "warm_start": batch_size,
                    "batch_size": batch_size,
                    "epsilon_decay_until": num_iterations,
                    "max_epsilon": 1.0,
                    "min_epsilon": 0.1,
                    "learning_rate": 0.001,
                    "capacity": {"long": capacity_max, "short": 15},
                    "semantic_decay_factor": 0.8,
                    "dqn_params": {
                        "gcn_layer_params": {
                            "type": "stare",
                            "embedding_dim": 64,
                            "num_layers": 2,
                            "gcn_drop": 0.1,
                            "triple_qual_weight": 0.8,
                        },
                        "relu_between_gcn_layers": True,
                        "dropout_between_gcn_layers": False,
                        "mlp_params": {
                            "num_hidden_layers": 2,
                            "dueling_dqn": True,
                        },
                        "use_raw_embeddings_for_qa": use_raw_embeddings_for_qa,
                    },
                    "num_samples_for_results": {"val": 2, "test": 2},
                    "plotting_interval": 50,
                    "train_seed": 5,
                    "test_seed": 0,
                    "device": "cpu",
                    "env_config": {
                        "question_prob": 1.0,
                        "terminates_at": terminates_at,
                        "randomize_observations": "all",
                        "room_size": "xl-different-prob",
                        "rewards": {"correct": 1, "wrong": 0, "partial": 0},
                        "make_everything_static": False,
                        "num_total_questions": 1000,
                        "question_interval": 1,
                        "include_walls_in_observations": True,
                    },
                    "default_root_dir": "training-results/TRASH",
                    "qa_function": "bandit",
                    "qa_entities": qa_entities,
                    "pretrained_path": pretrained_path,
                    "llm_params": None,
                }
                agent = DQNAgent(**params_dict)
                agent.train()
                agent.remove_results_from_disk()
