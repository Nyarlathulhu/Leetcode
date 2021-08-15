# RELATED TOPICS:
# Tree | Depth-First Search | Binary Search Tree | Binary Tree

# NOTE: This problem is the same as No.538.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def getSuccessor(node):
            successor = node.right
            while successor.left and successor.left != node:
                successor = successor.left
            return successor
        
        total = 0
        node = root
        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                successor = getSuccessor(node)
                if not successor.left:
                    successor.left = node
                    node = node.right
                else:
                    successor.left = None
                    total += node.val
                    node.val = total
                    node = node.left
        return root
    
