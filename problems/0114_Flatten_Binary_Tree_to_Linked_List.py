# RELATED TOPICS:
# Linked List | Stack | Tree | Depth-First Search | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flattenChild(node):
            if not node:
                return
            flattenChild(node.left)
            flattenChild(node.right)
            right = node.right
            node.right = node.left
            node.left = None
            while node.right:
                node = node.right
            node.right = right
        
        flattenChild(root)
        
