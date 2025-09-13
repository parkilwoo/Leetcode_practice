from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        문자열 s와 숫자 k가 주어졌을 때,
        원하는 문자열로 k번까지 변경이 가능할 때 반복되는 가장 긴 문자열의 길이
        """
        left = 0
        result = 0
        max_freq = 0
        freq_map = defaultdict(int)

        for right in range(len(s)):
            current_s = s[right]
            freq_map[current_s] += 1
            # 현재 윈도우내에서 가장 많이 나온 문자열의 길이
            max_freq = max(max_freq, freq_map[current_s])

            # 현재 윈도우내에서 가장 많이 나온 문자열의 길이 + k가 윈도우 사이즈보다 작을경우 left 이동
            window_size = right-left+1
            if (max_freq+k) < window_size:
                # left 이동을 하므로 freq_map에서 해당 값 1 다운
                left_s = s[left]
                freq_map[left_s] -= 1
                left += 1
                window_size -= 1

            result = max(result, window_size)

        return result
                