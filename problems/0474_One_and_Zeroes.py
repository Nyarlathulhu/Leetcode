# RELATED TOPICS:
# Array | String | Dynamic Programming

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        # memo = [[0] * (n + 1)] * (m + 1)
        for s in strs:
            count = collections.Counter(s)
            if '0' not in count:
                count['0'] = 0
            if '1' not in count:
                count['1'] = 0
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    if count['0'] <= i and count['1'] <= j:
                        memo[i][j] = max(memo[i][j], memo[i-count['0']][j-count['1']] + 1)
        return memo[-1][-1]
    
