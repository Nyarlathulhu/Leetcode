# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        memo = 1 << target
        for num in nums:
            memo |= memo >> num
        return memo % 2
    
