from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstWord = strs[0]
        res = ''
        for i in range(len(firstWord)):
            if all(word.startswith(firstWord[:i+1]) for word in strs):
                res = firstWord[:i+1]
            else:
                break
        return res