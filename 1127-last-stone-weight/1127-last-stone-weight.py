import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        
        # 최대 힙을 가져야 하므로 음수처리
        heap_list = [-s for s in stones]
        heapq.heapify(heap_list)

        while len(heap_list) > 1:
            y = heapq.heappop(heap_list)
            x = heapq.heappop(heap_list)

            if y - x < 0:
                heapq.heappush(heap_list, y - x)
        
        return abs(heap_list[0]) if heap_list else 0
            