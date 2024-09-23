class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_array = s.split()
        return len(str_array[-1])
