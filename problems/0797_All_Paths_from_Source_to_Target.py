# RELATED TOPICS:
# Backtracking | Depth-First Search | Breadth-First Search | Graph

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        path = collections.deque()
        n = len(graph)
        
        def traverse(s, path):
            path.append(s)
            if s == n - 1:
                res.append(list(path))
                path.pop()
                return
            for adj in graph[s]:
                traverse(adj, path)
            path.pop()
        
        traverse(0, path)
        return res
    
