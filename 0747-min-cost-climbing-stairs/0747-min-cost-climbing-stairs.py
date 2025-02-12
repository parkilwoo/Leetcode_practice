class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # f(n) = f(n-1) + cost(n-1) 
        #        f(n-2) + cost(n-2)
        cost_len = len(cost) + 1
        dp = [0] * cost_len
        for i in range(2, cost_len):
            one_step = dp[i-1] + cost[i-1]
            two_step = dp[i-2] + cost[i-2]
            dp[i] = min(one_step, two_step)
        
        return dp[cost_len - 1]