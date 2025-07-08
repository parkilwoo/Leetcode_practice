class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        1부터 n까지 포함하는 nums 배열에서 겹치는 수의 시작과 그 수의 연속되는 수를 배열로 리턴
        nums의 길이는 2부터 10000
        nums의 요소의 크기는 1부터 10000
        """
        duplicate = sum(nums) - sum(set(nums))
        not_exist = sum([i for i in range(1, len(nums)+1)]) - sum(set(nums))
        return [duplicate, not_exist]


        
        
            