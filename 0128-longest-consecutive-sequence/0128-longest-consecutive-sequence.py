class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        max_len = 0
        set_nums = set(nums) # in과 not in 연산을 O(1)로 만들기 위해
        
        for num in set_nums:
            # 현재의 숫자가 연속된 숫자의 처음 숫자일 경우 
            if (num-1) not in set_nums:
                length = 1
                # 현재 숫자의 다음 숫자가 set에 포함되어 있다면 연속된 숫자
                while num+length in set_nums:
                    length += 1
                max_len = max(max_len, length)
        
        return max_len

                
            
