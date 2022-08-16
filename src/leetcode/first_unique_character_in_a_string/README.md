# [387\. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)

## Description

Difficulty: **Easy**

Related Topics: [Hash Table](https://leetcode.com/tag/hash-table/), [String](https://leetcode.com/tag/string/), [Queue](https://leetcode.com/tag/queue/), [Counting](https://leetcode.com/tag/counting/)


Given a string `string`, find the first non-repeating character in it and return its
index. If it does not exist, return `-1`.

**Example 1:**

```
Input: string = "leetcode"
Output: 0
```

**Example 2:**

```
Input: string = "loveleetcode"
Output: 2
```

**Example 3:**

```
Input: string = "aabb"
Output: -1
```

**Constraints:**

*   1 <= string.length <= 10<sup>5</sup>
*   `s` consists of only lowercase English letters.


### Solution Starter Code
Language: **Python3**

```python3
class Solution:
    def firstUniqChar(self, string: str) -> int:
        pass
```

## Solution
The solution below seems to me like the most intuitive one while at the same time employing no modules outside of the standard library.

```python3
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
```

I want to write another solution for this problem using one of the [bounter](https://github.com/RaRe-Technologies/bounter) counter types. The difference in runtime and memory efficiency is absolutely remarkable. Of course, the first solution has to actually run in the LeetCode environment, so that was a non-starter, at least for the time being.
