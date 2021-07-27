# RELATED TOPICS:
# Array | Backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(start, target, comb, ans):
            if target == 0:
                return ans.append(comb + [])
            for i in range(start, len(candidates)):
                if target - candidates[i] >= 0:
                    comb.append(candidates[i])
                    DFS(i, target - candidates[i], comb, ans)
                    comb.pop()
        
        output = []
        DFS(0, target, [], output)
        return output
    
