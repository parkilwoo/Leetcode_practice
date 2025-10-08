class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        dp[m][n] = dp[m-1][n]+dp[m][n-1]
        """

        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                left = dp[i][j-1] if j > 0 else 0
                up = dp[i-1][j] if i > 0 else 0
                if i==0 and j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = left+up
        
        return dp[m-1][n-1]