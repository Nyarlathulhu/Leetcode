# RELATED TOPICS:
# Dynamic Programming | Tree | Depth-First Search | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def isRobbed(node):
            """
            return a 2 length list,
            list[0] is max amount if not rob this node,
            list[1] is max amount if rob this node
            """
            if not node:
                return [0, 0]
            rob_left = isRobbed(node.left)
            rob_right = isRobbed(node.right)
            robbed = node.val + rob_left[0] + rob_right[0]
            not_robbed = max(rob_left[0], rob_left[1]) + \
                              max(rob_right[0], rob_right[1])
            return [not_robbed, robbed]
        
        return max(isRobbed(root))
    
