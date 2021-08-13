# RELATED TOPICS:
# Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node_vals = []
        
        def constructMaximumBinaryTree(nums):
            if not nums:
                return None
            max_num = max(nums)
            idx = nums.index(max_num)
            root = TreeNode(val=max_num)
            root.left = constructMaximumBinaryTree(nums[:idx])
            root.right = constructMaximumBinaryTree(nums[idx+1:])
            return root
        
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            node_vals.append(node.val)
            traverse(node.right)
        
        traverse(root)
        node_vals.append(val)
        return constructMaximumBinaryTree(node_vals)
    
