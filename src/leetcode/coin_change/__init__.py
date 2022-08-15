"""LeetCode Problem 322 - Coin Change"""

from typing import List


def make_change(coins: List[int], amount: int) -> int:
    """Make Change

    Return the minimum number of coins required to make change with the coin denominations
    available to us. Also, if the amount is zero, the number of coins is also zero.
    """
    return -1


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        return make_change(coins, amount)
