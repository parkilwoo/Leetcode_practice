class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoization = {}
        for i in range(len(nums)):
            num_v = nums[i]
            minus_val = target - num_v
            if memoization.get(minus_val) is not None:
                return [memoization.get(minus_val), i]
            memoization[num_v] = i