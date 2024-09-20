from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        start = strs[0]
        last = strs[-1]
        longest_prefix = ""

        for i in range(min(len(start), len(last))):
            if start[i] != last[i]:
                return longest_prefix
            longest_prefix += start[i]

        return longest_prefix
