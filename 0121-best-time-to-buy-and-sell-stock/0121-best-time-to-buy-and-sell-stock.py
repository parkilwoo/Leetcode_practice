class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices[i]는 i번째날의 주식가격
        최대 이득이 되는 가격을 구하기(싸게 사서 비싸게 팔기)
        이득을 얻을 수 없으면(판매가가 구매가보다 높을경우) 0으로 리턴
        구매한 날보다 이전날에는 판매할 수 없음
        배열의 길이가 10만까지이므로 최대 O(NlogN) 으로 구현
        """
        profit = 0
        if len(prices) == 1:
            return profit
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell
        return profit
        