# RELATED TOPICS:
# Array | Backtracking

from itertools import combinations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        all_combs = [list(c) for c in combinations(nums, k)]
        output = []
        for comb in all_combs:
            if sum(comb) == n:
                output.append(comb)
        return output
    
