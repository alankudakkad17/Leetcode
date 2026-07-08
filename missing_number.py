class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=len(nums)
        number= l*(l+1)/2-sum(nums)
        return int(number)
