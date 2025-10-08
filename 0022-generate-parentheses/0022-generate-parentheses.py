class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(cur_str, open_cnt, close_cnt):
            if len(cur_str) == n*2:
                result.append(cur_str)
                return None
            
            if open_cnt < n:
                backtrack(cur_str+"(", open_cnt+1, close_cnt)
            if close_cnt < open_cnt:
                backtrack(cur_str+")", open_cnt, close_cnt+1)

        backtrack("", 0, 0)

        return result