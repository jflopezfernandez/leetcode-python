
from unittest import TestCase, skip

from leetcode.longest_consecutive_sequence import Solution


class TestSolution(TestCase):

    def test_example_one(self) -> None:
        self.assertEqual(Solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)

    def test_example_two(self) -> None:
        self.assertEqual(Solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9)

    def test_timeout_exceeded(self) -> None:
        self.assertEqual(Solution.longestConsecutive(long_thing), len(long_thing))
