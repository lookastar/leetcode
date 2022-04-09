class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        pos=len(s)-1
        trailing_spaces=0

        while s[pos]==' ' and pos>=0:
            pos -= 1
            trailing_spaces += 1

        while pos >= 0:
            if s[pos] == ' ':
                return len(s)-1 - pos - trailing_spaces
            pos -= 1
        return len(s) - trailing_spaces

