
from unittest import TestCase, skip

from leetcode.first_unique_character_in_a_string import Solution


class TestFirstUniqueCharacterInAString(TestCase):

    def test_single_character_strings(self) -> None:
        self.assertEqual(Solution.firstUniqChar('a'), 0)
        self.assertEqual(Solution.firstUniqChar('b'), 0)
        self.assertEqual(Solution.firstUniqChar('c'), 0)

    def test_double_characters(self) -> None:
        self.assertEqual(Solution.firstUniqChar('ab'), 0)
        self.assertEqual(Solution.firstUniqChar('aa'), -1)

    def test_case_example_one(self) -> None:
        self.assertEqual(Solution.firstUniqChar('leetcode'), 0)

    def test_case_example_two(self) -> None:
        self.assertEqual(Solution.firstUniqChar('loveleetcode'), 2)

    def test_case_example_three(self) -> None:
        self.assertEqual(Solution.firstUniqChar('aabb'), -1)
