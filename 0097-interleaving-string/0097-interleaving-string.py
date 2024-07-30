class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        if s1_len + s2_len != s3_len: return False
        if not s1_len and s2 == s3: return True
        if not s2_len and s1 == s3: return True

        dp = [[False for _ in range(s1_len + 1)] for _ in  range(s2_len + 1)]
        # 최초 값 True 초기화 
        dp[0][0] = True 
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i == 0 and j == 0: continue
                elif i == 0:
                    dp[i][j] = True if s1[:j] == s3[:j] else False
                elif j == 0:
                    dp[i][j] = True if s2[:i] == s3[:i] else False
                else:
                    dp[i][j] = True if (dp[i][j-1] and s1[j-1] == s3[i+j-1]) or (dp[i-1][j] and s2[i-1] == s3[i+j-1]) else False

        return dp[-1][-1] 
         