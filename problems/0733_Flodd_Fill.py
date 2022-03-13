# RELATED TOPICS
# Array | Depth-First Search | Breadth-First Search | Matrix

from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor != newColor:
            q = deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
                    if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor:
                        q.append((x, y))
        return image
      
