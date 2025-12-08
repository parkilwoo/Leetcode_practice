class Solution:
    def checkString(self, s: str) -> bool:
        "a가 다 나오고 b가 나와야 함"
        
        a_appear = False
        b_appear = False
        for ch in s:
            if ch == 'a':
                a_appear = True
                if b_appear:
                    return False
            else:
                b_appear = True
        return True
