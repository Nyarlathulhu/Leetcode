# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        min_income = -1001
        if k > len(prices) / 2:
            income_i_0 = 0
            income_i_1 = min_income
            for i in range(len(prices)):
                temp = income_i_0
                income_i_0 = max(income_i_0, income_i_1 + prices[i])
                income_i_1 = max(income_i_1, temp - prices[i])
            return income_i_0
        
        income = {}
        for j in range(k + 1):
            income[(-1, j, 0)] = 0
            income[(-1, j, 1)] = min_income
        for i in range(len(prices)):
            income[(i, 0, 0)] = 0
            income[(i, 0 ,1)] = min_income
            for t in range(1, k + 1):
                income[(i, t, 0)] = max(income[(i-1, t, 0)], income[(i-1, t, 1)] + prices[i])
                income[(i, t, 1)] = max(income[(i-1, t, 1)], income[(i-1, t-1, 0)] - prices[i])
        return income[(len(prices)-1, k, 0)]
    
