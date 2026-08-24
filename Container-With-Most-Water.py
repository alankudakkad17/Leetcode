class Solution:
    def maxWater(self, arr):
        n=len(arr)
        if n<=0:
            return 0
        left=0
        right=n-1
        maxi=0
        while left<right:
            dist=right-left
            dis=min(arr[right],arr[left])
            area=dis*dist
            maxi=max(maxi,area)
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1
        return maxi
