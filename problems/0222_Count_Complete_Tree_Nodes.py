# RELATED TOPICS
# Binary Search | Tree | Depth-First Search | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        l = root
        r = root
        h_left = 0
        h_right = 0
        
        while l:
            l = l.left
            h_left += 1
        while r:
            r = r.right
            h_right += 1
        
        # perfect binary tree
        if h_left == h_right:
            return 2 ** h_left - 1
        # complete binary tree
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
