class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 순열 만들기
        res = []

        def backtrack(pick, arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return None
            for i in range(len(nums)):
                if pick[i]:
                    continue
                pick[i] = True
                arr.append(nums[i])
                backtrack(pick, arr)
                pick[i] = False
                arr.pop()

        backtrack([False] * len(nums), [])
        return res