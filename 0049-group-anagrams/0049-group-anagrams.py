class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        문자열배열 strs가 주어졌을 때, anagram끼리 배열로 묶어서 리턴
        배열의 순서는 상관 없음
        Anagram 판단하는 방법
        """
        memoization = dict()
        group_idx = 0
        for string in strs:
            count = [0] * 26
            for s in string:
                count[ord(s) - ord('a')] += 1
            tuple_cnt = tuple(count)
            if tuple_cnt not in memoization:
                memoization[tuple_cnt] = list()
            memoization[tuple_cnt].append(string)

        return list(memoization.values())

        
                