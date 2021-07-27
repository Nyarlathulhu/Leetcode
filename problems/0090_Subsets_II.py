# RELATED TOPICS:
# Array | Backtracking | Bit Manipulation

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        subsets.append([])
        subset_size = 0
        for i in range(0, len(nums)):
            start = subset_size if i >= 1 and nums[i] == nums[i-1] else 0
            subset_size = len(subsets)
            for j in range(start, subset_size):
                subsets.append(subsets[j] + [nums[i]])
        return subsets
    
