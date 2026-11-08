class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        if not nums:
            return -1 
        di=set()
        for num in nums:
            if num in di:
                return num
            else:
                di.add(num)
