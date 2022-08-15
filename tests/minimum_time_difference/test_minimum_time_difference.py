
from unittest import TestCase, skip

from leetcode.minimum_time_difference import Solution


class TestSolution(TestCase):

    @skip('This problem has been successfully completed.')
    def test_wrap_around(self) -> None:
        self.assertEqual(Solution.findMinDifference(['23:59', '00:00']), 1)

    @skip('This problem has been successfully completed.')
    def test_wrap_around_with_duplicate(self) -> None:
        self.assertEqual(Solution.findMinDifference(['00:00', '23:59', '00:00']), 0)

    @skip('This problem has been successfully completed.')
    def test_one_hour_difference(self) -> None:
        self.assertEqual(Solution.findMinDifference(["01:01","02:01"]), 60)
