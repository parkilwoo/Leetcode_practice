class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_hash = {}
        for num in nums:
            if num not in count_hash:
                count_hash[num] = 0
            count_hash[num] = count_hash[num] + 1

        sorted_keys = sorted(count_hash.keys(), key=lambda item:count_hash.get(item), reverse=True)
        return sorted_keys[:k]
        