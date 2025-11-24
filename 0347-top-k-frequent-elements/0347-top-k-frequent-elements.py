from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 가장 많이 나온 갯수 뽑기
        num_counter = Counter(nums)

        # 1. sorting 방식
        # sorting = []
        # for num, cnt in num_counter.items():
        #     sorting.append((cnt, num))
        
        # sorting.sort()
        # res = []
        # while k > 0:
        #     res.append(sorting.pop()[1])
        #     k -= 1

        # return res

        # 2. maxHeap 방식
        heap = []

        for num, cnt in num_counter.items():
            heapq.heappush(heap, (-cnt, num))

        res = []
        while k > 0:
            _, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        return res
