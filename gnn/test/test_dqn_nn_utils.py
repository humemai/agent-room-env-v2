import unittest
from typing import Literal

import numpy as np
import torch

from agent.dqn.nn import GNN
from agent.dqn.nn.utils import (cconv, ccorr, com_mult, conj,
                                extract_entities_and_relations,
                                maybe_num_nodes, process_graph, rotate,
                                scatter_, softmax)

sample = [
    ["room_000", "south", "room_004", {"current_time": 18, "timestamp": [13]}],
    ["agent", "atlocation", "room_000", {"current_time": 18, "strength": 1.6}],
    ["room_001", "south", "room_005", {"timestamp": [12, 14], "strength": 1}],
]


class TestExtractEntitiesAndRelations(unittest.TestCase):
    def test_function(self):
        entities, relations = extract_entities_and_relations(sample)
        self.assertEqual(
            set(entities),
            set(
                [
                    "room_000",
                    "room_004",
                    "agent",
                    "room_001",
                    "room_005",
                    "18",
                    "13",
                    "2",
                    "14",
                    "1",
                ]
            ),
        )
        self.assertEqual(
            set(relations),
            set(
                [
                    "south",
                    "atlocation",
                    "timestamp",
                    "current_time",
                    "strength",
                    "south_inv",
                    "atlocation_inv",
                ]
            ),
        )


class TestProcessGraph(unittest.TestCase):
    def test_function(self):
        (
            entities,
            relations,
            edge_idx,
            edge_type,
            quals,
            edge_idx_inv,
            edge_type_inv,
            quals_inv,
            short_memory_idx,
            agent_entity_idx,
        ) = process_graph(sample)
        self.assertEqual(
            entities,
            [
                "room_005",
                "room_004",
                "room_001",
                "room_000",
                "agent",
                "2",
                "18",
                "14",
                "13",
                "1",
            ],
        )
        self.assertEqual(
            relations,
            [
                "timestamp",
                "strength",
                "south_inv",
                "south",
                "current_time",
                "atlocation_inv",
                "atlocation",
            ],
        )
        self.assertTrue(torch.equal(edge_idx, torch.tensor([[3, 4, 2], [1, 3, 0]])))
        self.assertTrue(torch.equal(edge_type, torch.tensor([3, 6, 3])))
        self.assertTrue(
            torch.equal(
                quals,
                torch.tensor(
                    [[4, 0, 4, 1, 0, 1], [6, 8, 6, 5, 7, 9], [0, 0, 1, 1, 2, 2]]
                ),
            )
        )
        self.assertTrue(torch.equal(edge_idx_inv, torch.tensor([[1, 3, 0], [3, 4, 2]])))
        self.assertTrue(torch.equal(edge_type_inv, edge_type_inv))
        self.assertTrue(torch.equal(quals, quals_inv))
        self.assertTrue(torch.equal(short_memory_idx, torch.tensor([0, 1])))
        self.assertEqual(agent_entity_idx, 4)
