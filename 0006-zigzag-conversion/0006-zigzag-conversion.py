class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        dp = [[""] * len(s) for _ in range(numRows)]
        
        down = 0
        right = 0
        is_bottom = False
        for v in s:
            if is_bottom == True:
                # i가 밑에 끝까지 도착하면 우상단으로 이동
                dp[down][right] = v
                if down == 0:
                    is_bottom = False
                    down += 1
                else:
                    down -= 1
                    right += 1
            else:
                dp[down][right] = v
                if down == numRows-1:
                    is_bottom = True
                    right += 1
                    down -= 1
                else:
                    down += 1
        result = ""
        for list_str in dp:
            result += ''.join(list_str)
        return result
