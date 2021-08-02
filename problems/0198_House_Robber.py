# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def rob(self, nums: List[int]) -> int:
        amount_i = amount_i_1 = amount_i_2 = 0
        for num in reversed(nums):
            amount_i = max(amount_i_1, num + amount_i_2)
            amount_i_2 = amount_i_1
            amount_i_1 = amount_i
        return amount_i
    
