# RELATED TOPICS:
# Array | Dynamic Programming

# standard DP
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_income = -100001
        max_transac = 2
        # (i, j, k) = (the i-th day, j transactions are done, got k stock)
        income = {
            (-1, 0, 0): 0,
            (-1, 0, 1): min_income,
            (-1, 1, 0): 0,
            (-1, 1, 1): min_income,
            (-1, 2, 0): 0,
            (-1, 2, 1): min_income
        }
        for i in range(len(prices)):
            income[(i, 0, 0)] = 0
            income[(i, 0 ,1)] = min_income
            for t in range(1, max_transac + 1):
                income[(i, t, 0)] = max(income[(i-1, t, 0)], income[(i-1, t, 1)] + prices[i])
                income[(i, t, 1)] = max(income[(i-1, t, 1)], income[(i-1, t-1, 0)] - prices[i])
        return income[(len(prices)-1, max_transac, 0)]


# simpler one, 39.6% runtime and 26.5% memory usage
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        income_i_1_0 = income_i_2_0 = 0
        income_i_1_1 = income_i_2_1 = -100001
        for price in prices:
            income_i_2_0 = max(income_i_2_0, income_i_2_1 + price)
            income_i_2_1 = max(income_i_2_1, income_i_1_0 - price)
            income_i_1_0 = max(income_i_1_0, income_i_1_1 + price)
            income_i_1_1 = max(income_i_1_1, -price)
        return income_i_2_0
    
