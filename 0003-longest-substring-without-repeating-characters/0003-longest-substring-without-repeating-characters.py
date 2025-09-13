class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        슬라이딩 윈도우는 일반적으로 두개의 포인터 left, right를 사용하여 문자열 혹은 배열의 특정 범위를 효율적으로 탐색하는 알고리즘. 마치 창문처럼 윈도우 크기를 줄이거나 확장하여 탐색 

        슬라이딩 윈도우의 원리
        1. 윈도우 확장: right 포인터를 오른쪽으로 이동시켜 윈도우의 크기를 확장. 이 과정에서 새로운 요소를 윈도우에 추가한다.
        2. 계산/판단: 윈도우 내의 요소들을 사용하여 문제 해결에 필요한 계산을 진행하거나 조건을 만족하는지 판단한다.
        3. 윈도우 축소: 만약 윈도우가 조건을 만족하지 못한다면, left 포인터를 오른쪽으로 이동시켜 윈도우의 크기를 줄인다. 이 과정에서 윈도우의 시작점이 변경된다.
        """

        str_idx_map = {}
        left = 0
        max_len = 0

        for right in range(len(s)):
            current = s[right]
            # 중복된 문자열이 있을경우 윈도우의 크기를 줄여야함.
            # LEFT = LEFT + 1
            if current in str_idx_map and str_idx_map[current] >= left:
                left = str_idx_map[current] + 1
            
            # 이전 문자의 위치를 업데이트
            str_idx_map[current] = right

            # 윈도우 사이즈 구하기
            window_size = right+1 - left
            max_len = max(max_len, window_size)

        return max_len