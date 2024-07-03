class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_value = 0
        check_dict = {}
        for idx, char in enumerate(s):
            if check_dict.get(char):
                max_value = max(max_value, len(check_dict))
                duplicate_idx = check_dict[char]
                check_dict.clear()
                for j in range(duplicate_idx+1, idx+1):
                    check_dict[s[j]] = j
                continue
            check_dict[char] = idx
        return max(max_value, len(check_dict))        