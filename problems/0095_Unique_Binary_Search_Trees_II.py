# RELATED TOPICS:
# Dynamic Programming | Backtracking | Tree | Binary Search Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            for i in range(low, high + 1):
                left_children = build(low, i - 1)
                right_children = build(i + 1, high)
                for left in left_children:
                    for right in right_children:
                        res.append(TreeNode(i, left, right))
            return res
        
        return build(1, n)
    
