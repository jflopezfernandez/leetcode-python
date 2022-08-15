
from unittest import TestCase

from leetcode.shortest_word_distance import Solution


class TestSolution(TestCase):

    def test_problem_examples(self) -> None:
        self.assertEqual(Solution.shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'coding', 'practice'), 3)
        self.assertEqual(Solution.shortestDistance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'), 1)

    def test_minimal_word_list(self) -> None:
        self.assertEqual(Solution.shortestDistance(['practice', 'makes'], 'makes', 'practice'), 1)
