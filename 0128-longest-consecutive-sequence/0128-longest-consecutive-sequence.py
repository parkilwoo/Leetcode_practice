class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        max_len = 0
        before_val = nums[0]
        cur_len = 1
        for i, num in enumerate(nums[1:]):
            if before_val == num:
                continue
            if before_val+1 == num:
                cur_len += 1
            else:
                if cur_len > max_len:
                    max_len = cur_len
                if max_len > len(nums)-i:
                    break
                cur_len = 1
            before_val = num

        return max(max_len, cur_len)

                
            
