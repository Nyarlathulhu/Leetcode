# RELATED TOPICS:
# Tree | Depth-First Search | Binary Search Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0
        node = root
        nodes = []
        while nodes or node:
            while node:
                nodes.append(node)
                node = node.right
            node = nodes.pop()
            total += node.val
            node.val = total
            node = node.left
        return root
        
