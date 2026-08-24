class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l=set(nums)
        if len(nums)>len(l):
            return True
        return False
