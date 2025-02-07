class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hash = {}
        for char in s:
            if s_hash.get(char):
                continue
            char_count = s.count(char)
            if char_count != t.count(char):
                return False
            s_hash[char] = char_count
        return True
            