
from collections import Counter
from typing import Dict, List, Text

from bounter import bounter


class Solution:

    @classmethod
    def firstUniqChar(cls, string: Text) -> int:
        """First Unique Character

        Return the index of the first non-repeating character in the string, if there is
        one. If there is no unique character in the input string, simply return -1.
        """
        # Initialize the lookup table we will be using to count how many times each
        # character is in the string.
        characters = Counter(string)

        # Iterate over each of the characters of the string, starting from the left. This
        # will ensure that running into multiple characters that appeared only once will
        # not cause problems.
        for index, character in enumerate(string):
            # The only thing that matters is that a character appeared only once in the
            # string. If more than one character meets that criteria, the tie goes to
            # whichever character appeared first.
            if characters[character] == 1:
                # Return the character's index.
                return index

        # If no character met the uniqueness criteria we simply return -1.
        return -1

    @classmethod
    def optimized(cls, string: Text) -> int:
        # Initialize the lookup table we will be using to check whether each character is
        # already in the set.
        tracker = bounter(size_mb=16, need_counts=True, need_iteration=True)

        # Once the lookup table has been initialized, we need to actually populate it with
        # the characters in the string.
        tracker.update(string)

        # TODO: Use the bounter extension to take advantage of the significantly higher
        # runtime and memory efficiency of its data structures.
        return -1
