class Solution:
    def climbStairs(self, n: int) -> int:
        # n번째 계단에 도달하는 방법은 n-1 -> 1칸 or n-2 -> 2칸
        # dp[n] = dp[n-1] + dp[n-2]
        if n < 2:
            return n
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]
