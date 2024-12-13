import unittest
from typing import Literal

import numpy as np
import torch

from agent.dqn.nn import GNN
from agent.dqn.utils import (ReplayBuffer, compute_loss_explore,
                             compute_loss_mm, console, find_non_masked_rows,
                             plot_results, save_final_results,
                             save_states_q_values_actions, save_validation,
                             select_action, target_hard_update, update_epsilon,
                             update_model)

batch = {
    "obs": np.array(
        [
            list(
                [
                    [
                        "room_000",
                        "south",
                        "room_004",
                        {"current_time": 18, "timestamp": [13]},
                    ],
                    ["dep_007", "atlocation", "room_000", {"current_time": 18}],
                    [
                        "agent",
                        "atlocation",
                        "room_000",
                        {"current_time": 18, "strength": 1.6},
                    ],
                    [
                        "dep_001",
                        "atlocation",
                        "room_000",
                        {"current_time": 18, "strength": 1},
                    ],
                    [
                        "room_000",
                        "east",
                        "room_001",
                        {"current_time": 18, "timestamp": [17]},
                    ],
                    ["room_000", "west", "wall", {"current_time": 18, "strength": 1}],
                    ["room_000", "north", "wall", {"current_time": 18, "strength": 1}],
                    ["room_004", "east", "room_005", {"strength": 1}],
                    ["room_001", "east", "wall", {"strength": 1.1096883200000003}],
                    [
                        "room_001",
                        "north",
                        "wall",
                        {"timestamp": [8, 12], "strength": 1.3312000000000002},
                    ],
                    ["agent", "atlocation", "room_005", {"timestamp": [11]}],
                    [
                        "room_001",
                        "south",
                        "room_005",
                        {"timestamp": [12, 14], "strength": 1},
                    ],
                    ["agent", "atlocation", "room_001", {"timestamp": [14, 16]}],
                ]
            ),
            list(
                [
                    ["room_002", "north", "wall", {"current_time": 46}],
                    ["room_002", "west", "wall", {"current_time": 46}],
                    [
                        "room_002",
                        "south",
                        "room_008",
                        {"current_time": 46, "timestamp": [40]},
                    ],
                    ["agent", "atlocation", "room_002", {"current_time": 46}],
                    ["room_002", "east", "room_003", {"current_time": 46}],
                    ["sta_007", "atlocation", "room_002", {"current_time": 46}],
                    [
                        "room_009",
                        "south",
                        "room_012",
                        {"strength": 1, "timestamp": [44]},
                    ],
                    ["room_003", "south", "room_009", {"timestamp": [38, 41]}],
                    ["room_003", "north", "wall", {"strength": 1}],
                    ["room_003", "west", "room_002", {"strength": 1}],
                    ["room_009", "east", "wall", {"strength": 1}],
                    ["room_009", "north", "room_003", {"timestamp": [42, 43, 44]}],
                    [
                        "room_009",
                        "west",
                        "room_008",
                        {"timestamp": [42, 44], "strength": 1},
                    ],
                    [
                        "ind_006",
                        "atlocation",
                        "room_009",
                        {"timestamp": [43], "strength": 1},
                    ],
                    [
                        "agent",
                        "atlocation",
                        "room_009",
                        {"strength": 1, "timestamp": [44]},
                    ],
                    ["sta_002", "atlocation", "room_008", {"timestamp": [45]}],
                    ["room_008", "west", "room_007", {"strength": 1}],
                ]
            ),
            list(
                [
                    [
                        "room_009",
                        "north",
                        "room_003",
                        {"current_time": 54, "timestamp": [52]},
                    ],
                    ["agent", "atlocation", "room_009", {"current_time": 54}],
                    ["room_009", "south", "room_012", {"current_time": 54}],
                    [
                        "room_009",
                        "east",
                        "wall",
                        {"current_time": 54, "timestamp": [52]},
                    ],
                    [
                        "room_009",
                        "west",
                        "room_008",
                        {"current_time": 54, "timestamp": [52]},
                    ],
                    ["room_002", "south", "room_008", {"strength": 1}],
                    ["room_002", "west", "wall", {"timestamp": [47]}],
                    ["room_003", "east", "wall", {"strength": 1.0649600000000001}],
                    ["room_003", "north", "wall", {"strength": 1, "timestamp": [50]}],
                    ["agent", "atlocation", "room_003", {"strength": 1}],
                    ["room_012", "east", "wall", {"strength": 1}],
                    ["room_012", "north", "room_009", {"timestamp": [53]}],
                    ["agent", "atlocation", "room_012", {"strength": 1}],
                    ["room_012", "west", "room_011", {"strength": 1}],
                ]
            ),
            list(
                [
                    [
                        "room_010",
                        "east",
                        "wall",
                        {
                            "current_time": 73,
                            "timestamp": [59, 63, 70],
                            "strength": 1.6,
                        },
                    ],
                    [
                        "room_010",
                        "west",
                        "wall",
                        {
                            "current_time": 73,
                            "strength": 1.8911744000000004,
                            "timestamp": [61, 62, 63, 64, 68, 70, 71],
                        },
                    ],
                    [
                        "room_010",
                        "south",
                        "room_014",
                        {
                            "current_time": 73,
                            "timestamp": [59, 69],
                            "strength": 1.4078404198400003,
                        },
                    ],
                    [
                        "room_010",
                        "north",
                        "room_006",
                        {
                            "current_time": 73,
                            "timestamp": [59, 62, 69],
                            "strength": 1.2800000000000002,
                        },
                    ],
                    [
                        "dep_004",
                        "atlocation",
                        "room_010",
                        {
                            "current_time": 73,
                            "strength": 1.2953600000000003,
                            "timestamp": [61, 66, 70],
                        },
                    ],
                    [
                        "agent",
                        "atlocation",
                        "room_010",
                        {
                            "current_time": 73,
                            "strength": 1.2615680000000005,
                            "timestamp": [61, 63, 66, 70, 72],
                        },
                    ],
                    ["room_007", "north", "wall", {"strength": 1}],
                    ["room_006", "south", "room_010", {"timestamp": [58]}],
                    ["agent", "atlocation", "room_006", {"strength": 1}],
                    ["agent", "atlocation", "room_014", {"timestamp": [65]}],
                    ["room_014", "north", "room_010", {"timestamp": [65]}],
                    ["room_014", "south", "room_019", {"timestamp": [65]}],
                ]
            ),
        ],
        dtype=object,
    ),
    "next_obs": np.array(
        [
            list(
                [
                    [
                        "dep_007",
                        "atlocation",
                        "room_000",
                        {"current_time": 19, "timestamp": [18]},
                    ],
                    [
                        "dep_001",
                        "atlocation",
                        "room_000",
                        {"current_time": 19, "strength": 1, "timestamp": [18]},
                    ],
                    ["room_000", "north", "wall", {"current_time": 19, "strength": 1}],
                    ["room_000", "south", "room_004", {"current_time": 19}],
                    [
                        "agent",
                        "atlocation",
                        "room_000",
                        {"current_time": 19, "strength": 2.08},
                    ],
                    [
                        "room_000",
                        "west",
                        "wall",
                        {"current_time": 19, "strength": 1, "timestamp": [18]},
                    ],
                    [
                        "room_000",
                        "east",
                        "room_001",
                        {"current_time": 19, "timestamp": [17]},
                    ],
                    ["room_004", "east", "room_005", {"strength": 1}],
                    ["room_001", "east", "wall", {"strength": 1}],
                    [
                        "room_001",
                        "north",
                        "wall",
                        {"timestamp": [8, 12], "strength": 1.0649600000000001},
                    ],
                    ["agent", "atlocation", "room_005", {"timestamp": [11]}],
                    [
                        "room_001",
                        "south",
                        "room_005",
                        {"timestamp": [12, 14], "strength": 1},
                    ],
                    ["agent", "atlocation", "room_001", {"timestamp": [14, 16]}],
                ]
            ),
            list(
                [
                    [
                        "sta_007",
                        "atlocation",
                        "room_002",
                        {"current_time": 47, "strength": 1},
                    ],
                    [
                        "room_002",
                        "north",
                        "wall",
                        {"current_time": 47, "timestamp": [46]},
                    ],
                    ["room_002", "west", "wall", {"current_time": 47}],
                    [
                        "agent",
                        "atlocation",
                        "room_002",
                        {"current_time": 47, "strength": 1},
                    ],
                    [
                        "room_002",
                        "east",
                        "room_003",
                        {"current_time": 47, "strength": 1},
                    ],
                    [
                        "room_002",
                        "south",
                        "room_008",
                        {"current_time": 47, "strength": 1},
                    ],
                    [
                        "room_009",
                        "south",
                        "room_012",
                        {"strength": 1, "timestamp": [44]},
                    ],
                    ["room_009", "east", "wall", {"strength": 1}],
                    ["room_009", "north", "room_003", {"timestamp": [42, 43, 44]}],
                    [
                        "room_009",
                        "west",
                        "room_008",
                        {"timestamp": [42, 44], "strength": 1},
                    ],
                    [
                        "ind_006",
                        "atlocation",
                        "room_009",
                        {"timestamp": [43], "strength": 1},
                    ],
                    [
                        "agent",
                        "atlocation",
                        "room_009",
                        {"strength": 1, "timestamp": [44]},
                    ],
                    ["sta_002", "atlocation", "room_008", {"timestamp": [45]}],
                ]
            ),
            list(
                [
                    ["room_008", "north", "room_002", {"current_time": 55}],
                    ["room_008", "east", "room_009", {"current_time": 55}],
                    ["room_008", "west", "room_007", {"current_time": 55}],
                    ["sta_002", "atlocation", "room_008", {"current_time": 55}],
                    ["room_008", "south", "room_011", {"current_time": 55}],
                    ["agent", "atlocation", "room_008", {"current_time": 55}],
                    ["room_002", "south", "room_008", {"strength": 1}],
                    ["room_003", "east", "wall", {"strength": 1}],
                    ["room_003", "north", "wall", {"strength": 1, "timestamp": [50]}],
                    ["agent", "atlocation", "room_003", {"strength": 1}],
                    ["room_009", "east", "wall", {"timestamp": [52], "strength": 1}],
                    ["room_009", "west", "room_008", {"timestamp": [52, 54]}],
                    ["room_009", "north", "room_003", {"timestamp": [52, 54]}],
                    ["room_012", "east", "wall", {"strength": 1}],
                    ["room_012", "north", "room_009", {"timestamp": [53]}],
                    ["agent", "atlocation", "room_012", {"strength": 1}],
                    ["agent", "atlocation", "room_009", {"timestamp": [54]}],
                    ["room_009", "south", "room_012", {"timestamp": [54]}],
                ]
            ),
            list(
                [
                    [
                        "room_010",
                        "west",
                        "wall",
                        {
                            "current_time": 74,
                            "strength": 1.5129395200000004,
                            "timestamp": [61, 62, 63, 64, 68, 70, 71],
                        },
                    ],
                    [
                        "dep_004",
                        "atlocation",
                        "room_010",
                        {
                            "current_time": 74,
                            "strength": 1.0362880000000003,
                            "timestamp": [61, 66, 70, 73],
                        },
                    ],
                    [
                        "room_010",
                        "north",
                        "room_006",
                        {
                            "current_time": 74,
                            "timestamp": [59, 62, 69, 73],
                            "strength": 1.0240000000000002,
                        },
                    ],
                    [
                        "room_010",
                        "south",
                        "room_014",
                        {
                            "current_time": 74,
                            "timestamp": [59, 69, 73],
                            "strength": 1.1262723358720004,
                        },
                    ],
                    [
                        "room_010",
                        "east",
                        "wall",
                        {
                            "current_time": 74,
                            "timestamp": [59, 63, 70],
                            "strength": 1.2800000000000002,
                        },
                    ],
                    [
                        "agent",
                        "atlocation",
                        "room_010",
                        {
                            "current_time": 74,
                            "strength": 1.8092544000000004,
                            "timestamp": [61, 63, 66, 70, 72],
                        },
                    ],
                    ["room_007", "north", "wall", {"strength": 1}],
                    ["room_006", "south", "room_010", {"timestamp": [58]}],
                    ["agent", "atlocation", "room_006", {"strength": 1}],
                    ["agent", "atlocation", "room_014", {"timestamp": [65]}],
                    ["room_014", "north", "room_010", {"timestamp": [65]}],
                    ["room_014", "south", "room_019", {"timestamp": [65]}],
                ]
            ),
        ],
        dtype=object,
    ),
    "acts_explore": np.array([3, 0, 3, 1]),
    "acts_mm": np.array(
        [
            np.array([1, 0, 1, 0, 2, 0, 2]),
            np.array([0, 2, 1, 1, 1, 1]),
            np.array([0, 0, 0, 1, 0]),
            np.array([2, 2, 0, 0, 0, 1]),
        ],
        dtype=object,
    ),
    "rews_explore": np.array([0.0, 1.0, 0.0, 0.0]),
    "rews_mm": np.array([0.0, 1.0, 0.0, 0.0]),
    "done": np.array([0.0, 0.0, 0.0, 0.0]),
}

entities = [
    "sta_000",
    "sta_001",
    "sta_002",
    "sta_003",
    "sta_004",
    "sta_005",
    "sta_006",
    "sta_007",
    "ind_000",
    "ind_001",
    "ind_002",
    "ind_003",
    "ind_004",
    "ind_005",
    "ind_006",
    "ind_007",
    "dep_000",
    "dep_001",
    "dep_002",
    "dep_003",
    "dep_004",
    "dep_005",
    "dep_006",
    "dep_007",
    "agent",
    "room_000",
    "room_001",
    "room_002",
    "room_003",
    "room_004",
    "room_005",
    "room_006",
    "room_007",
    "room_008",
    "room_009",
    "room_010",
    "room_011",
    "room_012",
    "room_013",
    "room_014",
    "room_015",
    "room_016",
    "room_017",
    "room_018",
    "room_019",
    "room_020",
    "room_021",
    "room_022",
    "room_023",
    "room_024",
    "room_025",
    "room_026",
    "room_027",
    "room_028",
    "room_029",
    "room_030",
    "room_031",
    "wall",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100",
]
relations = [
    "north",
    "east",
    "south",
    "west",
    "atlocation",
    "north_inv",
    "east_inv",
    "south_inv",
    "west_inv",
    "atlocation_inv",
    "current_time",
    "timestamp",
    "strength",
]


class TestReplayBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = ReplayBuffer(size=100, batch_size=32)

    def test_store(self):
        obs = {"state": 1}
        act_explore = 2
        act_mm = [0, 1]
        rew_explore = 2.0
        rew_mm = 1.0
        next_obs = {"state": 2}
        done = False

        self.buffer.store(obs, act_explore, act_mm, rew_explore, rew_mm, next_obs, done)

        self.assertEqual(self.buffer.size, 1)
        self.assertEqual(self.buffer.obs_buf[0], obs)
        self.assertEqual(self.buffer.acts_explore_buf[0], act_explore)
        self.assertEqual(self.buffer.acts_mm_buf[0], act_mm)
        self.assertEqual(self.buffer.rews_explore_buf[0], rew_explore)
        self.assertEqual(self.buffer.rews_mm_buf[0], rew_mm)
        self.assertEqual(self.buffer.next_obs_buf[0], next_obs)
        self.assertEqual(self.buffer.done_buf[0], done)

    def test_sample_batch(self):
        for i in range(50):
            self.buffer.store(
                {"state": i},
                i,
                [i],
                float(i) * 2,
                float(i),
                {"state": i + 1},
                i % 2 == 0,
            )

        batch = self.buffer.sample_batch()

        self.assertEqual(len(batch["obs"]), 32)
        self.assertEqual(len(batch["acts_explore"]), 32)
        self.assertEqual(len(batch["acts_mm"]), 32)
        self.assertEqual(len(batch["rews_explore"]), 32)
        self.assertEqual(len(batch["rews_mm"]), 32)
        self.assertEqual(len(batch["next_obs"]), 32)
        self.assertEqual(len(batch["done"]), 32)

        nums = [foo["state"] for foo in batch["obs"]]
        self.assertEqual(nums, [foo for foo in batch["acts_explore"]])
        self.assertEqual(nums, [foo[0] for foo in batch["acts_mm"]])
        self.assertEqual(nums, [float(foo) / 2 for foo in batch["rews_explore"]])
        self.assertEqual(nums, [foo for foo in batch["rews_mm"]])
        self.assertEqual(nums, [foo["state"] - 1 for foo in batch["next_obs"]])
        self.assertTrue(([foo % 2 == 0 for foo in nums] == batch["done"]).all())


class TestFindNonMaskedRows(unittest.TestCase):

    def test_simple_case(self):
        mask = torch.tensor([[[1, 1], [1, 1]], [[0, 0], [1, 1]], [[1, 1], [0, 0]]])
        expected = [torch.tensor([0, 1]), torch.tensor([1]), torch.tensor([0])]
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), len(expected))
        for res, exp in zip(result, expected):
            self.assertTrue(torch.equal(res, exp))

    def test_all_masked(self):
        mask = torch.zeros((2, 3, 4))
        expected = [torch.tensor([]), torch.tensor([])]
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), len(expected))
        for res, exp in zip(result, expected):
            self.assertTrue(torch.equal(res, exp))

    def test_all_unmasked(self):
        mask = torch.ones((2, 3, 4))
        expected = [torch.tensor([0, 1, 2]), torch.tensor([0, 1, 2])]
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), len(expected))
        for res, exp in zip(result, expected):
            self.assertTrue(torch.equal(res, exp))

    def test_mixed_case(self):
        mask = torch.tensor(
            [[[1, 0, 1], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [1, 1, 1], [0, 1, 0]]]
        )
        expected = [torch.tensor([0, 1, 2]), torch.tensor([1, 2])]
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), len(expected))
        for i, (res, exp) in enumerate(zip(result, expected)):
            print(f"Batch {i}:")
            print(f"Expected: {exp}")
            print(f"Result: {res}")
            self.assertTrue(torch.equal(res, exp))

    def test_single_batch(self):
        mask = torch.tensor([[[1, 1], [0, 0], [1, 0]]])
        expected = [torch.tensor([0, 2])]
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), len(expected))
        for res, exp in zip(result, expected):
            self.assertTrue(torch.equal(res, exp))

    def test_large_input(self):
        mask = torch.randint(0, 2, (10, 100, 50))
        result = find_non_masked_rows(mask)
        self.assertEqual(len(result), 10)
        for batch_result in result:
            self.assertTrue(torch.is_tensor(batch_result))
            self.assertTrue(batch_result.dim() == 1)
            self.assertTrue(batch_result.dtype == torch.long)


class TestComputeLoss(unittest.TestCase):

    def setUp(self):
        self.gnn = GNN(entities=entities, relations=relations)

    def test_compute_loss_mm(self):
        self.batch = {}
        self.batch["obs"] = batch["obs"]
        self.batch["next_obs"] = batch["next_obs"]
        self.batch["acts"] = batch["acts_mm"]
        self.batch["rews"] = batch["rews_mm"]
        self.batch["done"] = batch["done"]
        gamma = 0.99
        device = "cpu"

        for ddqn in [True, False]:
            loss = compute_loss_mm(self.batch, device, self.gnn, self.gnn, ddqn, gamma)
            self.assertTrue(loss.requires_grad)

    def test_compute_loss_explore(self):
        self.batch = {}
        self.batch["obs"] = batch["obs"]
        self.batch["next_obs"] = batch["next_obs"]
        self.batch["acts"] = batch["acts_explore"]
        self.batch["rews"] = batch["rews_explore"]
        self.batch["done"] = batch["done"]
        gamma = 0.99
        device = "cpu"

        for ddqn in [True, False]:
            loss = compute_loss_explore(
                self.batch, device, self.gnn, self.gnn, ddqn, gamma
            )
            self.assertTrue(loss.requires_grad)


class TestSelectAction(unittest.TestCase):
    def setUp(self):
        self.gnn = GNN(entities=entities, relations=relations)

    def test_select_action(self):
        state = batch["obs"][0]

        epsilon = 0.1

        action, q_values = select_action(state, True, self.gnn, epsilon, "mm")
        self.assertEqual(action.shape, (7,))
        self.assertEqual(q_values.shape, (7, 3))

        action, q_values = select_action(state, False, self.gnn, epsilon, "mm")
        self.assertEqual(action.shape, (7,))
        self.assertEqual(q_values.shape, (7, 3))

        action, q_values = select_action(state, True, self.gnn, epsilon, "explore")
        self.assertEqual(action.shape, (1,))
        self.assertEqual(q_values.shape, (1, 5))

        action, q_values = select_action(state, False, self.gnn, epsilon, "explore")
        self.assertEqual(action.shape, (1,))
        self.assertEqual(q_values.shape, (1, 5))
