# RELATED TOPICS:
# Array | Backtracking

from itertools import combinations


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(comb) for comb in combinations([i for i in range(1, n + 1)], k)]
    
