# RELATED TOPICS:
# Array | Hash Table

# less mem usage
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                return [i, nums.index(diff)]

# less runtime
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sums = {}
        for pos, val in enumerate(nums):
            if val not in dict_sums:
                dict_sums[target-val] = pos
            else:
                return [pos, dict_sums[val]]
        
