# RELATED TOPICS:
# Tree | Depth-First Search | Binary Search Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        while True:
            while root:
                nodes.append(root)
                root = root.left
            root = nodes.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
        
