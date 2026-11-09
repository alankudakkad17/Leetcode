class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        dp[0]=cost[0]
        dp[1]=cost[1]
        for x in range(2,n):
            dp[x]=cost[x]+min(dp[x-1],dp[x-2])
        dp[n]=min(dp[n-1],dp[n-2])
        return dp[n]
