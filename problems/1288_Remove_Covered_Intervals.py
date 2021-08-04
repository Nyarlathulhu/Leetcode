# RELATED TOPICS:
# Array | Sorting

# Warning: long runtime & large mem usage
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intvs = sorted(intervals, key=lambda y: y[0])
        start_set = sorted(list(set([x[0] for x in intvs])))
        intervals_sorted = []
        for start in start_set:
            same_start = []
            for interval in intvs:
                if interval[0] == start:
                    same_start.append(interval)
            same_start.sort(key=lambda x: x[1], reverse=True)
            intervals_sorted += same_start
        
        left = intervals_sorted[0][0]
        right = intervals_sorted[0][1]
        cover_count = 0
        for interval in intervals_sorted:
            if intervals_sorted.index(interval) == 0:
                continue
            if interval[0] >= left and interval[1] <= right:
                cover_count += 1
            elif interval[0] <= right and interval[1] >= right:
                right = interval[1]
            elif interval[0] > right:
                left = interval[0]
                right = interval[1]
        return len(intervals) - cover_count
    
