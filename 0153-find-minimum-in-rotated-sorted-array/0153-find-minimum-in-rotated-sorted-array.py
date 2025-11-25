class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # 오름차순이 안되는 순간을 포착
        min_v = nums[0]
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                min_v = min(min_v, nums[i])
                break
        return min_v
