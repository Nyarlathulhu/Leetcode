# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_income = -1001
        income_i_0 = income_pre = 0
        income_i_1 = min_income
        for price in prices:
            temp = income_i_0
            income_i_0 = max(income_i_0, income_i_1 + price)
            income_i_1 = max(income_i_1, income_pre - price)
            income_pre = temp
        return income_i_0
    
