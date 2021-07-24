# RELATED TOPICS:
# Array | Queue | Sliding Window | Heap (Priority Queue) | Monotonic Queue

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        maximums = []
        queue = deque()
        start = 0
        for loc, val in enumerate(nums):
            while queue and queue[-1] < val:
                queue.pop()
            queue.append(val)
            if loc >= k - 1:
                maximums.append(queue[0])
                if nums[start] == queue[0]:
                    queue.popleft()
                start += 1
        return maximums
        
