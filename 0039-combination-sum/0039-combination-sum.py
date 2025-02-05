class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        self.backtrack(answer, target, [], 0, candidates)
        return answer
    
    def backtrack(self, answer, remain: int, comb: List[int], index: int, candidates: List[int]):
        
        if remain == 0:
            answer.append(list(comb))
            return
        if remain < 0:
            return
        
        for i in range(index, len(candidates)):
            comb.append(candidates[i])
            self.backtrack(answer, remain - candidates[i], comb, i, candidates)
            comb.pop()
