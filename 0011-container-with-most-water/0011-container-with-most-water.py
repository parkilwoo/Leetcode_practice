class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 최대 면적의 크기 구하기
        # 면적의 크기는 밑변 * 높이: 밑변은 l과 r의 거리 높이는 heigt[l]과 height[r]의 최소값

        max_area = 0
        n = len(height)
        # 왼쪽, 오른쪽 pointer를 이용해서 크기 구하기
        l, r = 0, n-1
        while l < r:
            # 현재 포인터 위치에서의 크기
            left, right = height[l], height[r]
            distance = r-l
            if left > right:
                max_area = max(max_area, right * distance)
                r -= 1
            elif left < right:
                max_area = max(max_area, left * distance)
                l += 1
            else:
                max_area = max(max_area, left * distance)
                l += 1
        
        return max_area