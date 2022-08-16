
from unittest import TestCase, skip

from leetcode.minimum_time_difference import Solution


class TestSolution(TestCase):


    def test_wrap_around(self) -> None:
        self.assertEqual(Solution.findMinDifference(['23:59', '00:00']), 1)


    def test_wrap_around_with_duplicate(self) -> None:
        self.assertEqual(Solution.findMinDifference(['00:00', '23:59', '00:00']), 0)


    def test_one_hour_difference(self) -> None:
        self.assertEqual(Solution.findMinDifference(["01:01","02:01"]), 60)
