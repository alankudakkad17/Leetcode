class Solution:
    def climbStairs(self, n: int) -> int:
        ways=[]
        ways.append(1)
        ways.append(1)
        i=1
        for x in range(n):
            i+=1
            x=ways[i-1]+ways[i-2]
            ways.append(x)
        return ways[n]
