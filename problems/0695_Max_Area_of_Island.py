# RELATED TOPICS
# Array | Depth-First Search | Breadth-First Search |  Union Find | Matrix

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not any(sum(grid, [])):
            return 0
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    area = 0
                    q = collections.deque([(i, j)])
                    visited.add((i, j))
                    while q:
                        x, y = q.popleft()
                        area += 1
                        for r, c in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1 and (r, c) not in visited:
                                q.append((r, c))
                                visited.add((r, c))
                    max_area = max(max_area, area)
        return max_area
      
