class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        memoization = {}
        for num in nums:
            if memoization.get(num):
                return num
            memoization[num] = True
        