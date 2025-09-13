class Solution:
    def isValid(self, s: str) -> bool:
        set_dict = {
            ')': '(',
            '}': '{',
            ']': '['
        } 

        stack = []
        for ch in s:
            if ch in set_dict:
                if not stack:
                    return False
                op = stack.pop()
                if op != set_dict[ch]:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0