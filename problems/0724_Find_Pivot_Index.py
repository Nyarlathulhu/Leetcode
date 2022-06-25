# RELATED TOPICS
# Array | Prefix Sum

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        prefix_sum = 0
        for i, n in enumerate(nums):
            if prefix_sum == all_sum - prefix_sum - n:
                return i
            prefix_sum += n
        return -1
    
