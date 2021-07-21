# RELATED TOPICS:
# Depth-First Search | Breadth-First Search | Union Find | Graph

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        num = len(isConnected)
        idx = list(range(len(isConnected)))
        tree_sizes = [1] * len(isConnected)
        visited = set()
        
        def find(p):
            while p != idx[p]:
                p = idx[p]
            return p
        
        def connected(p, q):
            if find(p) == find(q):
                return True
            else:
                return False
            
        for city in range(len(isConnected)):
            if city not in visited:
                visited.add(city)
                adj = 0
                for i in isConnected[city]:
                    if i == 1 and adj != city and not connected(city, adj):
                        p_id = find(city)
                        q_id = find(adj)
                        if tree_sizes[p_id] < tree_sizes[q_id]:
                            idx[p_id] = q_id
                            tree_sizes[q_id] += tree_sizes[p_id]
                        else:
                            idx[q_id] = p_id
                            tree_sizes[p_id] += tree_sizes[q_id]
                        num -= 1
                    adj += 1
        return num
                
