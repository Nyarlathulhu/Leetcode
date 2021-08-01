# RELATED TOPICS:
# Array | Dynamic Programming

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the i-th day
        # 0: no stock yesterday, 1: bought stock yesterday
        income_i_0 = 0
        income_i_1 = -10001
        for price in prices:
            income_i_0 = max(income_i_0, income_i_1 + price)
            income_i_1 = max(income_i_1, -price)
        return income_i_0
    
