class Solution:
    def productExceptSelf(self, arr):
        # code here
        n=len(arr)
        preprod=[1]*n
        sufprod=[1]*n
        result=[0]*n
        
        for i in range(1,n):
            preprod[i]=arr[i-1]*preprod[i-1]
        for j in range(n-2,-1,-1):
            sufprod[j]=arr[j+1]*sufprod[j+1]
        for i in range(n):
            result[i]=preprod[i]*sufprod[i]
        return result
        
