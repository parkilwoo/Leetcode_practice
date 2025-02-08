import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        reverse_str = lower_str[::-1]
        return lower_str == reverse_str