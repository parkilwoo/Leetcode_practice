class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        정수형 배열 nums가 있을 때, 부분배열의 합 중 가자 큰 값을 구하기
        특정 구간(i, j | j>i)까지의 부분합 = prefix_sum[j] - prefix_sum[i]
        
        중요한건 이전까지의 누적합이 음수면 계속 더해도 최대값에 도움을 주지않음 -> 그러므로 시작점을 변경할 필요가 있음
        """

        prefix_sum = 0
        max_score = -float('inf')
        for num in nums:
            prefix_sum = max(num, prefix_sum+num)
            max_score = max(max_score, prefix_sum)

        return max_score
