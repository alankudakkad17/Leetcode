class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long=0
        f=set()
        left=0
        for right in range(len(s)):
            while s[right] in f:
                f.remove(s[left])
                left += 1

            f.add(s[right])
            long=max(long,right-left+1)
        return long
