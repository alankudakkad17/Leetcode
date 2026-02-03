class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        x=sorted(nums)
        lenght=len(x)
        current=1
        longest=1
        for y in range(1,lenght):
            if (x[y]==x[y-1]):
                continue
            elif(x[y]==x[y-1]+1):
                current+=1
            else:
                longest = max(longest, current)
                current = 1
        return max(longest, current)
