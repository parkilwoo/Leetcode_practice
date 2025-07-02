class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        비어있지 않은 정수형 array가 있고, 1개의 원소를 제외하고 모든 원소는 2개가 존재한다.
        이 중 1개의 원소를 찾아내자.
        linear runtime complexity를 해야하므로 최대 O(N)으로 구현 필요
        """
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums)-1
        memo = {}
        while left <= right:
            if left == right:
                v = nums[left]
                if memo.get(v):
                    del memo[v]
                else:
                    memo[v] = True
            else:
                v_list = (nums[left], nums[right])
                for v in v_list:
                    if memo.get(v):
                        del memo[v]
                    else:
                        memo[v] = True
            left += 1
            right -= 1
        
        return list(memo.keys())[0]