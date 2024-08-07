class Solution:
    def isHappy(self, n: int) -> bool:
        memoization = {}
        while not memoization.get(n):
            memoization[n] = True
            squares_list = [int(i) * int(i) for i in str(n)]
            n = sum(squares_list)
            if n == 1:
                return True
        return False