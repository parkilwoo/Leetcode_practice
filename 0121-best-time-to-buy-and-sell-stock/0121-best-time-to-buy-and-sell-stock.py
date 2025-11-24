class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices[i]는 i번째날의 주식가격
        최대 이득이 되는 가격을 구하기(싸게 사서 비싸게 팔기)
        이득을 얻을 수 없으면(판매가가 구매가보다 높을경우) 0으로 리턴
        구매한 날보다 이전날에는 판매할 수 없음
        배열의 길이가 10만까지이므로 최대 O(NlogN) 으로 구현
        """
        res = 0
        n = len(prices)
        # dp[i] = i번째 날까지 살 수 있던 주식의 최소값
        dp = [0] * n
        dp[0] = prices[0]
        for i in range(1, n):
            price = prices[i]
            dp[i] = min(dp[i-1], price)
            res = max(res, price-dp[i])
        
        return res
        