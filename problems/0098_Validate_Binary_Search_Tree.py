# RELATED TOPICS:
# Tree | Depth-First Search | Binary Search Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, node, min_node, max_node):
        if not node:
            return True
        if (min_node and node.val <= min_node.val) or \
           (max_node and node.val >= max_node.val):
            return False
        return self.isValid(node.left, min_node, node) and \
               self.isValid(node.right, node, max_node)
    
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, None, None)
    
