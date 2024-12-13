import unittest

import numpy as np
import torch

from agent.utils import (argmax, get_duplicate_dicts, list_duplicates_of,
                         positional_encoding)


class TestUtils(unittest.TestCase):

    def test_argmax(self):
        """Test the argmax function."""
        self.assertEqual(argmax([1, 3, 2, 4]), 3)
        self.assertEqual(argmax([-1, -3, -2, -4]), 0)
        self.assertEqual(argmax([1]), 0)

    def test_get_duplicate_dicts(self):
        """Test the get_duplicate_dicts function."""
        search = {"a": 1, "b": 2}
        target = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2}, {"a": 1}, {"b": 2}]
        expected = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2}]
        self.assertEqual(get_duplicate_dicts(search, target), expected)

        search = {"a": 1}
        target = [{"a": 1, "b": 2}, {"a": 2, "b": 1}, {"b": 2}, {"c": 3}]
        expected = [{"a": 1, "b": 2}]
        self.assertEqual(get_duplicate_dicts(search, target), expected)

        search = {"a": 3}
        expected = []
        self.assertEqual(get_duplicate_dicts(search, target), expected)

    def test_list_duplicates_of(self):
        """Test the list_duplicates_of function."""
        seq = [1, 2, 3, 2, 1, 2, 4]
        item = 2
        expected = [1, 3, 5]
        self.assertEqual(list_duplicates_of(seq, item), expected)

        item = 1
        expected = [0, 4]
        self.assertEqual(list_duplicates_of(seq, item), expected)

        item = 5
        expected = []
        self.assertEqual(list_duplicates_of(seq, item), expected)

    def test_positional_encoding(self):
        """Test the positional_encoding function."""
        positions = 5
        dimensions = 4

        # Test return type as numpy array
        pos_enc_np = positional_encoding(positions, dimensions, return_tensor=False)
        self.assertIsInstance(pos_enc_np, np.ndarray)
        self.assertEqual(pos_enc_np.shape, (positions, dimensions))

        # Test return type as PyTorch tensor
        pos_enc_torch = positional_encoding(positions, dimensions, return_tensor=True)
        self.assertIsInstance(pos_enc_torch, torch.Tensor)
        self.assertEqual(pos_enc_torch.shape, (positions, dimensions))

        # Ensure positional encoding is consistent
        self.assertTrue(np.allclose(pos_enc_np, pos_enc_torch.numpy()))

        # Ensure dimensions must be even
        with self.assertRaises(AssertionError):
            positional_encoding(positions, 3)
