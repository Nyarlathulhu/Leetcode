# RELATED TOPICS:
# Tree | Breadth-First Search | Binary Tree

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.val % 2 == 0:
            return False
        
        nodes = []
        nodes.append(root)
        # level index
        idx = 0
        
        while nodes:
            idx += 1
            for _ in range(len(nodes)):
                node = nodes.pop(0)
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            node_vals = [i.val for i in nodes]
                    
            # if there is at least an odd integer,
            # or not in decreasing order for odd-indexed level,
            # return false
            if idx % 2 == 1 and \
                (any([vertex.val % 2 for vertex in nodes]) or \
                 len(node_vals) != len(set(node_vals)) or \
                 node_vals != sorted(node_vals, reverse=True)):
                return False
            # if there is at least an even integer,
            # or not in increasing order for even-indexed level,
            # return false
            if idx % 2 == 0 and \
                (not all([vertex.val % 2 for vertex in nodes]) or \
                 len(node_vals) != len(set(node_vals)) or \
                 node_vals != sorted(node_vals)):
                return False
        
        return True
    
