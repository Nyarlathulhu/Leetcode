# RELATED TOPICS:
# Array | Backtracking

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def DFS(candidate_tags, start, target, comb, ans):
            if target == 0:
                ans.append(comb + [])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if target - candidates[i] < 0:
                    return 0
                if not candidate_tags[i]:
                    comb.append(candidates[i])
                    candidate_tags[i] = True
                    DFS(candidate_tags, i + 1, target - candidates[i], comb, ans)
                    comb.pop()
                    candidate_tags[i] = False
        
        output = []
        candidates.sort()
        candidate_tags = [False] * len(candidates)
        DFS(candidate_tags, 0, target, [], output)
        return output
    
