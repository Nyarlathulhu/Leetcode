# RELATED TOPICS:
# Math | Dynamic Programming | Recursion | Memoization

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        pprev = 0
        prev = 1
        for i in range(2, n + 1):
            cur = pprev + prev
            pprev = prev
            prev = cur
        return cur
    
