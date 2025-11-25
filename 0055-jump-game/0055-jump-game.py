class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 현재 위치에서 가장 멀리 갈 수 있는곳을 갱신
        max_idx = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i > max_idx:
                return False
            if max_idx >= n-1:
                return True
            max_idx = max(max_idx, i+num)
        
        return False