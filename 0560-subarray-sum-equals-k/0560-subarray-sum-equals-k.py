from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        정수 배열 nums가 있을 때, 부분배열의 합이 k가 될 때 부분배열의 갯수를 리턴?

        어떤 구간(i, j | j>i)의 부분배열의 부분합 = prefix_sum[j] - prefix_sum[i] = k
        prefix_sum[i] = prefix_sum[j] - k

        즉 현재 누적합에서 k를 뺀 값이 과거의 누적합에 몇번 등장했는지 확인
        """
        prefix_sum = 0
        prefix_sum_map = defaultdict(int)
        prefix_sum_map[0] = 1
        cnt = 0

        for num in nums:
            # 누적합
            prefix_sum += num
            if prefix_sum - k in prefix_sum_map:
                cnt += prefix_sum_map[prefix_sum - k]
            # 현재까지 누적합 개수 기록
            prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1

        return cnt

        
