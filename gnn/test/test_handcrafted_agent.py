import logging

logger = logging.getLogger()
logger.disabled = True

import random
import unittest

from tqdm.auto import tqdm

from agent import HandcraftedAgent


class HandcraftedAgentTest(unittest.TestCase):
    def test_all_agents(self) -> None:
        terminates_at = 4
        for mm_policy in ["random", "episodic", "semantic", "handcrafted"]:
            for qa_function in ["latest_strongest", "latest", "strongest", "random"]:
                for explore_policy in ["random", "avoid_walls"]:
                    for capacity_long in [6]:
                        for pretrain_semantic in [
                            False,
                            "include_walls",
                            "exclude_walls",
                        ]:
                            for semantic_decay_factor in [0.8]:
                                for seed in range(1):
                                    agent = HandcraftedAgent(
                                        env_str="room_env:RoomEnv-v2",
                                        env_config={
                                            **{
                                                "question_prob": 1.0,
                                                "seed": 42,
                                                "terminates_at": terminates_at,
                                                "room_size": random.choice(
                                                    [
                                                        "xxs-different-prob",
                                                        "xs",
                                                        "s-different-prob",
                                                        "m",
                                                        "l-different-prob",
                                                    ]
                                                ),
                                                "randomize_observations": "all",
                                                "make_everything_static": False,
                                                "rewards": {
                                                    "correct": 1,
                                                    "wrong": 0,
                                                    "partial": 0,
                                                },
                                                "num_total_questions": 100,
                                                "question_interval": 1,
                                            },
                                            "seed": seed,
                                        },
                                        mm_policy=mm_policy,
                                        qa_function=qa_function,
                                        explore_policy=explore_policy,
                                        num_samples_for_results=2,
                                        capacity={
                                            "long": capacity_long,
                                            "short": 15,
                                        },
                                        pretrain_semantic=pretrain_semantic,
                                        semantic_decay_factor=semantic_decay_factor,
                                        default_root_dir="training-results/TRASH",
                                    )
                                    agent.test()

                                    self.assertEqual(
                                        agent.num_semantic_decayed,
                                        terminates_at + 1,
                                    )

                                    agent.remove_results_from_disk()
                                    print(agent.scores)
