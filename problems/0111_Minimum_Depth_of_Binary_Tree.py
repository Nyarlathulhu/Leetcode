# RELATED TOPICS:
# Tree | Depth-First Search | Breadth-First Search | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 1
        q = Queue()
        q.put(root)
        while not q.empty():
            q_len = q.qsize()
            for _ in range(q_len):
                node = q.get()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            depth += 1
        return depth
    
