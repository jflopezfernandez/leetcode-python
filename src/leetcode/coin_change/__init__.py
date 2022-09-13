"""LeetCode Problem 322 - Coin Change"""

from typing import Dict, List, Optional


def make_change(coins: List[int], amount: int) -> int:
    """Make Change

    Return the minimum number of coins required to make change with the coin denominations
    available to us. Also, if the amount is zero, the number of coins is also zero.

    TODO: The case ([186, 419, 83, 408], 6249), 26) is taking forever because we are
    trying every single combination. What we could do is sort the list of coins in reverse
    order to try the biggest coins first, which would mean that the first solution is the
    optimal one.

    The runtime complexity of sorting the list of coins would be O(n log n), but since the
    runtime complexity of the current algorithm is O(n^n), where n is the number of coins,
    this is actually a massive improvement.
    """
    if not coins or amount < 0:
        return -1

    if amount == 0:
        return 0

    minimum = None

    for coin in coins:
        number_of_coins = make_change(coins, amount - coin)

        if number_of_coins == -1:
            continue

        if not minimum or minimum > number_of_coins:
            minimum = 1 + number_of_coins

    return minimum if minimum else -1


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        return make_change(coins, amount)
