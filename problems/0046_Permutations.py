# RELATED TOPICS:
# Array | Backtracking

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, temp):
            if not nums:
                res.append(temp[:])
                return 
            for i in range(len(nums)):
                temp.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], temp)
                temp.pop()
        
        backtrack(nums, [])
        return res
    
