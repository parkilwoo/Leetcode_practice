class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if j - i <= len(longest): break
                if self._check_palindrome(s[i:j]):
                    if len(longest) < j - i:
                        longest = s[i:j]
                    break
        return longest
    
    def _check_palindrome(self, s: str) -> bool:
        len_ = len(s)
        for i in range(len_ // 2):
            if s[i] != s[len_ -i -1]:
                return False
        return True