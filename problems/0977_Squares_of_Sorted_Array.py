# RELATED TOPICS
# Array | Two Pointers | Sorting

# worse than trivial method
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums_sq = [0] * len(nums)
        l, r = 0, len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                nums_sq[i] = nums[r] ** 2
                r -= 1
            else:
                nums_sq[i] = nums[l] ** 2
                l += 1
        return nums_sq
      
