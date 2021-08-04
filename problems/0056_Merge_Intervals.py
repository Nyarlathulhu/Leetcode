# RELATED TOPICS:
# Array | Sorting

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intvs = sorted(intervals, key=lambda x: x[0])
        ans = []
        ans.append(intvs[0])
        for i in range(1, len(intvs)):
            if intvs[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intvs[i][1], ans[-1][1])
            else:
                ans.append(intvs[i])
        return ans
    
