
from unittest import TestCase, skip

from leetcode.coin_change import Solution


class TestSolution(TestCase):


    def test_single_coin_change(self) -> None:
        self.assertEqual(Solution().coinChange([1], 1), 1)
        self.assertEqual(Solution().coinChange([2], 2), 1)
        self.assertEqual(Solution().coinChange([3], 3), 1)


    def test_ignore_superfluous_coin(self) -> None:
        self.assertEqual(Solution().coinChange([1, 2], 2), 1)


    def test_must_skip_first_coin(self) -> None:
        self.assertEqual(Solution().coinChange([1, 2], 1), 1)


    def test_zero_amount_results_in_zero_coins(self) -> None:
        self.assertEqual(Solution().coinChange([1], 0), 0)
        self.assertEqual(Solution().coinChange([2], 0), 0)
        self.assertEqual(Solution().coinChange([3], 0), 0)


    def test_backtracking_required(self) -> None:
        self.assertEqual(Solution().coinChange([2, 3], 7), 3)


    def test_edge_cases(self) -> None:
        self.assertEqual(Solution().coinChange([1], 0), 0)


    def test_impossible_cases(self) -> None:
        self.assertEqual(Solution().coinChange([2], 3), -1)


    def test_coins_out_of_order(self) -> None:
        self.assertEqual(Solution().coinChange([2, 5, 10, 1], 13), 3)
        self.assertEqual(Solution().coinChange([2, 5, 10, 1], 27), 4)


    def test_large_unordered_inputs(self) -> None:
        self.assertEqual(Solution().coinChange([186, 419, 83, 408], 6249), 26)


    def test_correct_cases(self) -> None:
        self.assertEqual(Solution().coinChange([1, 2, 3], 2), 1)
        self.assertEqual(Solution().coinChange([1, 2, 3], 3), 1)
        self.assertEqual(Solution().coinChange([1, 2, 3], 4), 2)
        self.assertEqual(Solution().coinChange([1, 2, 3], 5), 2)
        self.assertEqual(Solution().coinChange([1, 2, 3], 6), 2)
        self.assertEqual(Solution().coinChange([1, 2, 5], 11), 3)
