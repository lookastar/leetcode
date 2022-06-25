class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        if needle_len == 0: return 0

        possible_start = len(haystack) - len(needle)
        for i in range(0,possible_start +1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1