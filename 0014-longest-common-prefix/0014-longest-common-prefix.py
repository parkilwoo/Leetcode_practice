class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]

        for v in strs[1:]:
            idx = 0
            prefix_str = ""
            while not (idx == len(v) or idx == len(result)):
                if v[idx] == result[idx]:
                    prefix_str += v[idx]
                    idx += 1
                else:
                    break
            result = prefix_str
            if not result: break
        
        return result
                