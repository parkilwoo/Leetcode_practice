class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        부분수열의 합이 K와 같은 갯수 찾기
        nums의 길이는 1부터 200000
        각 요소는 -1000 ~ 1000까지 가능
        """
        result = 0

        # 1. Brute force 방식 O(N**2)
        # for i in range(len(nums)):
        #     total_sum = nums[i]
        #     if total_sum == k:
        #         result += 1
        #     for j in range(i+1, len(nums)):
        #         total_sum += nums[j]
        #         if total_sum == k:
        #             result += 1

        # return result
        
        # 2. 부분합 방식
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prefix_sum[i] = prefix_sum[i-1] + num
        # prefix_sum[i] - prefix_sum[j-1] = k
        # prefix_sum[j-1] = prefix_sum[i] - k
        # 즉, 현재까지의 누적합에서 k(목표값)를 뺀 값이 과거에 몇번 나왔는지 확인하면 됨

        # prefix_sum의 갯수가 몇개인지 확인하는 hash
        count = {0: 1}
        
        for prefix in prefix_sum:
            if prefix - k in count:
                result += count.get(prefix-k)
            count[prefix] = count.get(prefix, 0) + 1

        return result