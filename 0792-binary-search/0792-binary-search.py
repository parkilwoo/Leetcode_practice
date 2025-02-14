class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0] or target > nums[-1]:
            return -1

        l_idx, r_idx = 0, len(nums) - 1
        while l_idx <= r_idx:
            m_idx = (l_idx + r_idx) // 2

            m_idx_value = nums[m_idx]
            if target == m_idx_value:
                return m_idx
            if target > m_idx_value:
                l_idx = m_idx +1
                continue
            if target < m_idx_value:
                r_idx = m_idx - 1
                continue
        
        return -1
            
