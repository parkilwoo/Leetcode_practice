class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        배열 nums가 있을 때, 2개를 선택하여 target에 일치하는 인덱스를 return
        정확하게 1개의 답이 있음

        memoization을 이용해서 현재 선택된 값과 target의 차이가 memo에 있는지 체크
        pre+cur=k
        pre=k-cur
        """
        
        v_idx_map = {}

        for i, num in enumerate(nums):
            minus = target-num
            if minus in v_idx_map:
                return [v_idx_map[minus], i]
            v_idx_map[num] = i
