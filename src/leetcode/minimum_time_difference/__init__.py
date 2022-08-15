"""LeetCode Problem 539 - Minimum Time Difference

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes
difference between any two time-points in the list.
"""

from heapq import heappop, heappush
from sys import maxsize
from typing import List, Text


class Solution:

    @classmethod
    def findMinDifference(cls, time_points: List[Text]) -> int:
        queue: List[Text] = []

        for time_point in time_points:
            hours, minutes = time_point.split(':')
            hours, minutes = int(hours), int(minutes)
            time = hours * 60 + minutes
            heappush(queue, time)

        minimum = heappop(queue)
        maximum = minimum + (24 * 60)
        heappush(queue, maximum)
        heappush(queue, minimum)

        minimum_difference = maxsize

        a = heappop(queue)
        b = heappop(queue)

        while True:
            minimum_difference = min(minimum_difference, abs(a - b))

            if not queue:
                break

            a, b = b, heappop(queue)

        return minimum_difference
