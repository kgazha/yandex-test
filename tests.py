import unittest

from test_gazha import find_difference, remove_zeros


class ArrayTest(unittest.TestCase):

    def test_difference(self):
        n1 = [1, 1, 1, 2, 5, 3, 7]
        n2 = [1, 5]

        expected_result = [2, 3, 7]
        result = find_difference(n1, n2)

        self.assertEqual(expected_result, result)

    def test_remove_zeros(self):
        nums = [1, 0, 1, 2, 5, 0, 0, 7]

        expected_result = [1, 1, 2, 5, 7]
        result = remove_zeros(nums)

        self.assertEqual(expected_result, result)

    def test_remove_zeros_returns_empty_list(self):
        nums = [0, 0, 0]

        expected_result = []
        result = remove_zeros(nums)

        self.assertEqual(expected_result, result)
