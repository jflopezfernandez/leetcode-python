"""Problem 128 - Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.
"""

from typing import List


class Solution:

    @classmethod
    def longestConsecutive(cls, numbers: List[int]) -> int:
        numbers_set = set(numbers)
        maximum = 0

        while numbers_set:
            length = 1
            current = min(numbers_set)
            numbers_set.difference_update([current])

            while (current := current + 1) in numbers_set:
                length += 1
                numbers_set.difference_update([current])

            maximum = max(maximum, length)

        return maximum
