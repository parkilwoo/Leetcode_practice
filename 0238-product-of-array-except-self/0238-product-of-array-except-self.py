class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. brute force
        n = len(nums)
        res = [1] * n
        # for i in range(n):
        #     prod = 1
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         prod *= nums[j]
        #     res[i] = prod
        # return res

        # 나를 제외한 곱의 값: 나의 왼쪽 곱 * 나의 오른쪽 곱
        # f(i) = left(i) * right(i)
        # left(i) = nums[0] * num[1] * ...nums[i-1]
        # right(i) = nums[i+1] * nums[i+2] * ... num[n-1]
        left = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        right = [1] * n
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        res = [0] * n
        for i in range(n):
            res[i] = left[i] * right[i]

        return res
