class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 오늘의 가격이 어제보다 비싸면 무조건 어제 사고 오늘 판다를 반복
        
        profit = 0
        y_price = prices[0]
        n = len(prices)

        for i in range(1, n):
            t_price = prices[i]
            # 오늘의 가격이 어제보다 비싸면 무조건 profit에 추가
            if t_price - y_price > 0:
                profit += t_price - y_price
            y_price = t_price
        
        return profit
            