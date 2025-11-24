class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. brute force
        n = len(nums)
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
        res = [0] * n

        left_val = 1
        for i in range(n):
            res[i] = left_val
            left_val *= nums[i]
        
        right_val = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_val
            right_val *= nums[i]

        return res

