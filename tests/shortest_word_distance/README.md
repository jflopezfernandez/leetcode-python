# [243\. Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/)

## Description

Difficulty: **Easy**

Related Topics: [Array](https://leetcode.com/tag/array/), [String](https://leetcode.com/tag/string/)


Given an array of strings `wordsDict` and two different strings that already exist in the array `word1` and `word2`, return _the shortest distance between these two words in the list_.

**Example 1:**

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
```

**Example 2:**

```
Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1
```

**Constraints:**

*   2 <= wordsDict.length <= 3 * 10<sup>4</sup>
*   `1 <= wordsDict[i].length <= 10`
*   `wordsDict[i]` consists of lowercase English letters.
*   `word1` and `word2` are in `wordsDict`.
*   `word1 != word2`


## Solution

Language: **Python3**

```python3
"""LeetCode Problem 243 - Shortest Word Distance
​
Given an array of strings wordsDict and two different strings that already exist in the
array word1 and word2, return the shortest distance between these two words in the list.
"""
​
from itertools import product
from sys import maxsize
from typing import List, Text
​
​
class Solution:
​
    @classmethod
    def shortestDistance(cls, words: List[Text], word_1: Text, word_2: Text) -> int:
        indices = {}
​
        for index, word in enumerate(words):
            if word not in indices:
                indices[word] = {index}
                continue
​
            indices[word].add(index)
​
        minimum_distance = maxsize
​
        for i1, i2 in product(indices[word_1], indices[word_2]):
            distance = abs(i2 - i1)
​
            if not minimum_distance or distance < minimum_distance:
                minimum_distance = distance
​
        return minimum_distance
​
```
