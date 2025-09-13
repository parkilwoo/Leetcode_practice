class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        문자열 배열 strs가 주어졌을 때, 아나그램끼리 리스트로 묶어서 return
        아나그램은 특정 문자의 순열이면 됨
        """
        
        hash_map = {}
        for s in strs:
            ord_list = [0] * 26
            for ch in s:
                ord_list[ord(ch) - ord('a')] += 1
            
            key = tuple(ord_list)
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]

        return list(hash_map.values())
