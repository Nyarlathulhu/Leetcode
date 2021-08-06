# RELATED TOPICS:
# Tree | Depth-First Search | Breadth-First Search | Binary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def connectNodes(node1, node2):
            if not node1 or not node2:
                return
            node1.next = node2
            connectNodes(node1.left, node1.right)
            connectNodes(node2.left, node2.right)
            connectNodes(node1.right, node2.left)
        
        if not root:
            return None
        connectNodes(root.left, root.right)
        return root
    
