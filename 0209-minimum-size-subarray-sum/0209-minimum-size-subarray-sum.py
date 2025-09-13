class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        부분배열에서의 합이 target보다 크거나 같은 가장 작은 배열의 길이 수
        없다면 0 리턴
        """
        
        left = 0
        window_sum = 0
        min_len = float('inf')

        for right, num in enumerate(nums):
            window_sum += num
            
            while window_sum >= target:
                window_size = right - left + 1
                min_len = min(min_len, window_size)
                window_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0
        