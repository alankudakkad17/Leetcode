class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for x in range(len(digits)-1,-1,-1):
            if digits[x]<9:
                digits[x]=digits[x]+1
                return digits
            digits[x]=0
        return [1]+digits
