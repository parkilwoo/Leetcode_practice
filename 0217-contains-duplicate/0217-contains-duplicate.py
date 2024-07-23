class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        convert_set = set(nums)
        return len(convert_set) != len(nums)
        