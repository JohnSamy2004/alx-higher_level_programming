#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 5, 7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -5, -7]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -5, 7]), 7)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, 3, -5, 7.5]), 7.5)

if __name__ == '__main__':
    unittest.main()
