# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def rob(self, nums: List[int]) -> int:
        def robRange(start, end):
            amount_i = amount_i_1 = amount_i_2 = 0
            for i in reversed(range(start, end + 1)):
                amount_i = max(amount_i_1, nums[i] + amount_i_2)
                amount_i_2 = amount_i_1
                amount_i_1 = amount_i
            return amount_i
        
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(robRange(0, n - 2), robRange(1, n - 1))
    
