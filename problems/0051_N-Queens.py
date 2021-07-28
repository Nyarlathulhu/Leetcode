# RELATED TOPICS:
# Array | Backtracking

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        col = [0] * n
        diag1 = [0] * (n * 2)
        diag2 = [0] * (n * 2)
        cur = [0] * n

        def backtrack(row):
            if row == n:
                temp = []
                for i, j in enumerate(cur):
                    temp.append('.' * j + 'Q' + '.' * (n - j - 1))
                res.append(temp)
                return
            for i, taken in enumerate(col):
                if taken or diag1[row+i] or diag2[n-1+i-row]:
                    continue
                col[i], diag1[row+i], diag2[n-1+i-row] = 1, 1, 1
                cur[row] = i
                backtrack(row + 1)
                col[i], diag1[row+i], diag2[n-1+i-row] = 0, 0, 0
        
        backtrack(0)
        return res
    
