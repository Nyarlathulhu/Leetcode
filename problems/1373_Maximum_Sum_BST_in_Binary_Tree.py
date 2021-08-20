# RELATED TOPICS:
# Dynamic Programming | Tree | Depth-First Search | Binary Search Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def traverse(node):
            """
            return: (list)[isBST, min, max, sum]
            
            isBST: boolean, is a BST or not
            min: int, min value in subtree
            max: int, max value in subtree
            sum: int, sum of keys in subtree
            """
            nonlocal max_sum
            if not node:
                return [True, 40001, -40001, 0]
            left = traverse(node.left)
            right = traverse(node.right)
            if left[0] and right[0] and \
               node.val > left[2] and node.val < right[1]:
                res = [
                    True,
                    min(left[1], node.val),
                    max(right[2], node.val),
                    left[3] + right[3] + node.val
                ]
                max_sum = max(max_sum, res[3])
            else:
                res = [False]
            return res
        
        traverse(root)
        return max_sum
    
