# RELATED TOPICS:
# Array | Dynamic Programming | Greedy

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        income_i_0 = 0
        income_i_1 = -10001
        for price in prices:
            temp = income_i_0
            income_i_0 = max(income_i_0, income_i_1 + price)
            income_i_1 = max(income_i_1, temp - price)
        return income_i_0
    
