class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1을 재배열한 순열이 s2에 포함되어 있는지 확인
        s1 크기만큼의 윈도우로 체크
        """
        n1 = len(s1)
        n2 = len(s2)
        if n2 < n1:
            return False
        
        left = 0
        s1_freq = [0] * 26
        s2_freq = [0] * 26
        for i in range(n1):
            ord_s1 = ord(s1[i]) - ord('a')
            ord_s2 = ord(s2[i]) - ord('a')
            s1_freq[ord_s1] += 1
            s2_freq[ord_s2] += 1
        
        # 처음 시도에 성공할 경우
        if s1_freq == s2_freq:
            return True

        for right in range(n1, n2):
            current = s2[right]
            right_ord = ord(current) - ord('a')
            left_ord = ord(s2[left]) - ord('a')
            s2_freq[right_ord] += 1
            s2_freq[left_ord] -= 1
            if s1_freq == s2_freq:
                return True
            left +=1

        return False
            