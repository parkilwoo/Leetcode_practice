class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []

        def backtrack(open_count, close_count, n):
            if open_count == close_count == n:
                result.append("".join(stack))
                return
            
            if open_count < n:
                stack.append("(")
                backtrack(open_count+1, close_count, n)
                stack.pop()
            
            if open_count > close_count:
                stack.append(")")
                backtrack(open_count, close_count+1, n)
                stack.pop()

        backtrack(0, 0, n)
        return result