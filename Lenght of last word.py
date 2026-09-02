class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        x=s.split()
        return len(x[-1])
