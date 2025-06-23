class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        for i in range(len(s)):
            memo = {s[i]: True}
            for j in range(i+1, len(s)):
                v = s[j]
                if memo.get(v) is not None:
                    break
                memo[v] = True
            if max_len < len(memo):
                max_len = len(memo)
            if max_len >= len(s) - i:
                break
        return max_len

