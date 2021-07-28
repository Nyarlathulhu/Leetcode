# RELATED TOPICS:
# Array | Dynamic Programming | Breadth-First Search

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp_table = [amount + 1] * (amount + 1)
        dp_table[0] = 0
        for i in range(len(dp_table)):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp_table[i] = min(dp_table[i], dp_table[i-coin] + 1)
        return -1 if dp_table[amount] == amount + 1 else dp_table[amount]
    
