class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        k=0
        for x in nums:
            if x==target:
                return k
            elif x<target: 
                k=k+1
        return k
