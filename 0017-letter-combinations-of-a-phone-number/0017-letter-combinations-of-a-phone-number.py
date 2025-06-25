class Solution:
    _hash_map = {
        2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'],
        5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'],
        8: ['t','u','v'], 9: ['w','x','y','z']
    }    
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result

        def dfs(n, s):
            if len(s) == len(digits):
                result.append(s)
                return

            digit = int(digits[n])
            for v in self._hash_map[digit]:
                dfs(n+1, s+v)

        dfs(0, "")
        return result

        