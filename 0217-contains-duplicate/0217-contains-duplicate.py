class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for num in nums:
            if nums_dict.get(num):
                return True
            nums_dict[num] = True
        return False