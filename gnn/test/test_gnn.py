import unittest

import numpy as np
import torch

from agent.dqn.nn import GNN
from agent.dqn.nn.utils import process_graph

sample0 = [
    ["room_000", "south", "room_004", {"current_time": 18, "timestamp": [13]}],
    ["agent", "atlocation", "room_000", {"current_time": 18, "strength": 1.6}],
    ["room_001", "south", "room_005", {"timestamp": [12, 14], "strength": 1}],
]
sample1 = [
    ["sta_002", "atlocation", "room_000", {"timestamp": [45]}],
    ["room_005", "west", "room_007", {"strength": 1}],
    ["agent", "atlocation", "room_000", {"current_time": 18, "strength": 1.6}],
]
sample2 = [
    ["agent", "atlocation", "room_008", {"current_time": 55}],
    ["room_004", "south", "room_008", {"timestamp": [1, 2, 10], "strength": 1}],
]
data = np.array([sample0, sample1, sample2], dtype=object)


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


class TestGNNStarE(unittest.TestCase):
    def setUp(self):
        self.gnn = GNN(
            entities,
            relations,
            gcn_layer_params={
                "type": "StarE",
                "embedding_dim": 4,
                "num_layers": 2,
                "gcn_drop": 0.0,
                "triple_qual_weight": 0.8,
            },
            relu_between_gcn_layers=True,
            dropout_between_gcn_layers=False,
            mlp_params={"num_hidden_layers": 2, "dueling_dqn": True},
            rotational_for_relation=True,
            device="cpu",
        )

        (
            self.entities0,
            self.relations0,
            self.edge_idx0,
            self.edge_type0,
            self.quals0,
            self.edge_idx_inv0,
            self.edge_type_inv0,
            self.quals_inv0,
            self.short_memory_idx0,
            self.agent_entity_idx0,
        ) = process_graph(sample0)

        (
            self.entities1,
            self.relations1,
            self.edge_idx1,
            self.edge_type1,
            self.quals1,
            self.edge_idx_inv1,
            self.edge_type_inv1,
            self.quals_inv1,
            self.short_memory_idx1,
            self.agent_entity_idx1,
        ) = process_graph(sample1)

        (
            self.entities2,
            self.relations2,
            self.edge_idx2,
            self.edge_type2,
            self.quals2,
            self.edge_idx_inv2,
            self.edge_type_inv2,
            self.quals_inv2,
            self.short_memory_idx2,
            self.agent_entity_idx2,
        ) = process_graph(sample2)

        (
            self.entity_embeddings,
            self.relation_embeddings,
            self.edge_idx,
            self.edge_type,
            self.quals,
            self.short_memory_idx,
            self.num_short_memories,
            self.agent_entity_idx,
        ) = self.gnn.process_batch(data)

        self.q_mm = self.gnn(data, "mm")
        self.q_explore = self.gnn(data, "explore")

        self.q_mm0 = self.gnn(np.array([sample0]), "mm")
        self.q_mm1 = self.gnn(np.array([sample1]), "mm")
        self.q_mm2 = self.gnn(np.array([sample2]), "mm")

        self.q_explore0 = self.gnn(np.array([sample0]), "explore")
        self.q_explore1 = self.gnn(np.array([sample1]), "explore")
        self.q_explore2 = self.gnn(np.array([sample2]), "explore")

    def test_entity_embeddings(self):

        a = self.gnn.entity_embeddings[
            torch.tensor([self.gnn.entity_to_idx[e] for e in self.entities0])
        ]
        b = self.gnn.entity_embeddings[
            torch.tensor([self.gnn.entity_to_idx[e] for e in self.entities1])
        ]
        c = self.gnn.entity_embeddings[
            torch.tensor([self.gnn.entity_to_idx[e] for e in self.entities2])
        ]

        entity_embeddings = torch.cat([a, b, c, a, b, c], dim=0)

        self.assertTrue(torch.equal(self.entity_embeddings, entity_embeddings))

    def test_relation_embeddings(self):

        a = self.gnn.relation_embeddings[
            torch.tensor([self.gnn.relation_to_idx[r] for r in self.relations0])
        ]
        b = self.gnn.relation_embeddings[
            torch.tensor([self.gnn.relation_to_idx[r] for r in self.relations1])
        ]
        c = self.gnn.relation_embeddings[
            torch.tensor([self.gnn.relation_to_idx[r] for r in self.relations2])
        ]

        relation_embeddings = torch.cat([a, b, c, a, b, c], dim=0)

        self.assertTrue(torch.equal(self.relation_embeddings, relation_embeddings))

    def test_edge_idx(self):

        edge_idx = torch.cat(
            [
                self.edge_idx0,
                self.edge_idx1 + len(self.entities0),
                self.edge_idx2 + len(self.entities0) + len(self.entities1),
                self.edge_idx_inv0
                + len(self.entities0)
                + len(self.entities1)
                + len(self.entities2),
                self.edge_idx_inv1
                + len(self.entities0)
                + len(self.entities1)
                + len(self.entities2)
                + len(self.entities0),
                self.edge_idx_inv2
                + len(self.entities0)
                + len(self.entities1)
                + len(self.entities2)
                + len(self.entities0)
                + len(self.entities1),
            ],
            dim=1,
        )

        self.assertTrue(torch.equal(self.edge_idx, edge_idx))

    def test_edge_type(self):
        edge_type = torch.cat(
            [
                self.edge_type0,
                self.edge_type1 + len(self.relations0),
                self.edge_type2 + len(self.relations0) + len(self.relations1),
                self.edge_type_inv0
                + len(self.relations0)
                + len(self.relations1)
                + len(self.relations2),
                self.edge_type_inv1
                + len(self.relations0)
                + len(self.relations1)
                + len(self.relations2)
                + len(self.relations0),
                self.edge_type_inv2
                + len(self.relations0)
                + len(self.relations1)
                + len(self.relations2)
                + len(self.relations0)
                + len(self.relations1),
            ],
            dim=0,
        )
        self.assertTrue(torch.equal(self.edge_type, edge_type))

    def test_quals(self):
        quals = torch.cat(
            [
                self.quals0,
                self.quals1
                + torch.tensor(
                    [
                        [len(self.relations0)],
                        [len(self.entities0)],
                        [self.edge_idx0.shape[1]],
                    ],
                ),
                self.quals2
                + torch.tensor(
                    [
                        [len(self.relations0) + len(self.relations1)],
                        [len(self.entities0) + len(self.entities1)],
                        [self.edge_idx0.shape[1] + self.edge_idx1.shape[1]],
                    ],
                ),
            ],
            dim=1,
        )
        quals = quals.repeat(1, 2)
        self.assertTrue(torch.equal(self.quals, quals))

    def test_short_memory_idx(self):
        short_memory_idx = torch.cat(
            [
                self.short_memory_idx0,
                self.short_memory_idx1 + self.edge_idx0.shape[1],
                self.short_memory_idx2
                + self.edge_idx0.shape[1]
                + self.edge_idx1.shape[1],
            ],
            dim=0,
        )
        self.assertTrue(torch.equal(self.short_memory_idx, short_memory_idx))

    def test_agent_entity_idx(self):
        agent_entity_idx = torch.tensor(
            [
                self.agent_entity_idx0,
                self.agent_entity_idx1 + len(self.entities0),
                self.agent_entity_idx2 + len(self.entities0) + len(self.entities1),
            ]
        )

        self.assertTrue(torch.equal(agent_entity_idx, self.agent_entity_idx))

    def test_q_mm(self):
        self.assertEqual(len(self.q_mm), 3)
        self.assertEqual(len(self.q_mm0), 1)
        self.assertEqual(len(self.q_mm1), 1)
        self.assertEqual(len(self.q_mm2), 1)

        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm[0].shape), torch.tensor([2, 3]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm0[0].shape), torch.tensor([2, 3]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm1[0].shape), torch.tensor([1, 3]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm1[0].shape), torch.tensor([1, 3]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm2[0].shape), torch.tensor([1, 3]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_mm2[0].shape), torch.tensor([1, 3]))
        )

    def test_q_explore(self):
        self.assertEqual(len(self.q_explore), 3)
        self.assertEqual(len(self.q_explore0), 1)
        self.assertEqual(len(self.q_explore1), 1)
        self.assertEqual(len(self.q_explore2), 1)

        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore[0].shape), torch.tensor([1, 5]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore0[0].shape), torch.tensor([1, 5]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore1[0].shape), torch.tensor([1, 5]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore1[0].shape), torch.tensor([1, 5]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore2[0].shape), torch.tensor([1, 5]))
        )
        self.assertTrue(
            torch.equal(torch.tensor(self.q_explore2[0].shape), torch.tensor([1, 5]))
        )
