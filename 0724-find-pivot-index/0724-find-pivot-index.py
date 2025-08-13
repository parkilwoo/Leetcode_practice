class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # 누적합
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prefix_sum[i] = prefix_sum[i-1] + num        

        # 0~k까지의 부분합과 k~n까지의 부분합이 같은 위치 찾기
        for i in range(len(prefix_sum)):
            # pivot이 i일 경우 left = 0~i-1, right = i+1~n
            left = prefix_sum[i-1] if i != 0 else 0
            right = prefix_sum[len(prefix_sum)-1] - prefix_sum[i]
            if left == right:
                return i

        return -1