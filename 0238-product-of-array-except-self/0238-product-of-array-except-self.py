class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        정수배열 nums가 주어졌을 때, 
        answer를 리턴해라
        answer[i] = nums[i]를 제외한 nums모든 요소들의 곱

        어떤 위치 a에서 자신을 제외한 곱들의 값은?
        -> a의 왼쪽 곱 * a의 오른쪽 
        
        """
        
        n = len(nums)
        result = [1] * n

        # 본인을 제외한 왼쪽 누적곱 적용
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        
        # 본인을 제외한 오른쪽 누적 곱
        prefix_right = 1
        for i in range(n-1, -1, -1):
            result[i] *= prefix_right
            prefix_right *= nums[i]

        return result

        
        
        
            
