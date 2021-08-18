# RELATED TOPICS:
# Math | Dynamic Programming | Tree | Binary Search Tree | Binary Tree

class Solution:
    def numTrees(self, n: int) -> int:
        memo = []
        for _ in range(n + 1):
            memo.append([0] * (n + 1))
        
        def count(low, high):
            if low > high:
                return 1
            if memo[low][high] != 0:
                return memo[low][high]
            res = 0
            for i in range(low, high + 1):
                left = count(low, i - 1)
                right = count(i + 1, high)
                res += left * right
            memo[low][high] = res
            return res
        
        return count(1, n)
    
