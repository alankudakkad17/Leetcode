class Solution:
    def reverse(self, x: int) -> int:
        num=curr=rem=0
        temp=abs(x)
        sign=-1 if x<0 else 1 
        while temp > 0:  
            rem = temp % 10     
            num = num * 10 + rem  
            temp = temp // 10
        if num < -(2**31) or num > (2**31) - 1:
            return 0
        return num*sign
