class Solution:
    def maxWater(self, arr):
        l=0
        r=len(arr)-1
        base=0
        area=0
        while l<r:
            base=r-l
            area=max(area,base*min(arr[l],arr[r]))
            if arr[l] < arr[r]:
                l += 1
            else:
                r -= 1
        return area
        
