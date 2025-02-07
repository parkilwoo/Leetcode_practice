class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        bracket_couple = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for bracket in s:
            if bracket_couple.get(bracket):
                if not stack_list:
                    return False
                if stack_list.pop() != bracket_couple.get(bracket):
                    return False
            else:
                stack_list.append(bracket)

        if not stack_list:
            return True
        return False
