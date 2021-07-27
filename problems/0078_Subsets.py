# RELATED TOPICS:
# Array | Backtracking | Bit Manipulation

from itertools import combinations


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        output.append([])
        for i in range(1, len(nums) + 1):
            for subset in [list(comb) for comb in combinations(nums, i)]:
                output.append(subset)
        return output
    
