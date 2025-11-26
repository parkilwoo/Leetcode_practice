class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 정수형 배열 nums가 주어졌을 때, k개 만큼의 부분 배열의 평균이 가장 큰 값을 리턴
        
        before_sum = sum(nums[0:k])
        max_avg = before_sum / k
        n = len(nums)
        
        for i in range(1, n-k+1):
            sum_v = before_sum - nums[i-1] + nums[i+k-1]
            max_avg = max(max_avg, sum_v/k)
            before_sum = sum_v
        
        return max_avg