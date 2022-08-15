"""LeetCode Problem 243 - Shortest Word Distance

Given an array of strings wordsDict and two different strings that already exist in the
array word1 and word2, return the shortest distance between these two words in the list.
"""

from itertools import product
from sys import maxsize
from typing import List, Text


class Solution:

    @classmethod
    def shortestDistance(cls, words: List[Text], word_1: Text, word_2: Text) -> int:
        # Initialize the lookup table that we will use for storing the indices of each of
        # the entries in the word list.
        indices = {}

        # Begin iterating over each word, taking advantage of the enumerate utility to get
        # the index of each entry in the word list as well.
        for index, word in enumerate(words):
            # If the word is not already in the word list we need to add it in. To do this
            # we create a set at the appropriate entry in the lookup table.
            if word not in indices:
                indices[word] = {index}

                # Adding an item multiple times to the same set doesn't actually do
                # anything, so we technically don't need this return statement here, but
                # there's no point wasting CPU cycles for no reason.
                continue

            # If the current word is already in the lookup table, simply add the next
            # index to this entry's set.
            indices[word].add(index)

        # Initialize the minimum distance variable to something outrageously massive so we
        # can be sure there will be no confusion.
        minimum_distance = maxsize

        # Iterate over all of the indices of each word as pairs.
        for i1, i2 in product(indices[word_1], indices[word_2]):
            # The distance between two words is the absolute distance between their
            # indices.
            distance = abs(i2 - i1)

            # If this is the smallest distance we have seen so far, then this is the
            # current minimum distance, by definition.
            if distance < minimum_distance:
                # Update the current minimum distance entry and keep going.
                minimum_distance = distance

        # Once we've finally obtained the minimum distance, we simply return it.
        return minimum_distance
