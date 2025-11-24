class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 연속된 부분배열의 최대값을 구하는 것
        # 연속된 부분 배열의 합이 음수일 경우 더할 필요가 없음 -> 새로 시작

        res = -float('inf')
        
        sum_val = 0
        for num in nums:
            sum_val += num
            res = max(res, sum_val)
            if sum_val < 0:
                sum_val = 0
        return res