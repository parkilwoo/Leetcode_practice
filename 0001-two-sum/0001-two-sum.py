class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_sub = {}
        for i in range(len(nums)):
            num = nums[i]
            if hash_sub.get(num) is not None:
                return [hash_sub.get(num), i]
            sub_val = target - nums[i]
            hash_sub[sub_val] = i