# RELATED TOPICS:
# Array | Hash Table | Divide and Conquer | Tree | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(left, right, mapping, preorder, inorder):
            if left > right:
                return None
            root = TreeNode(val=preorder.pop(0))
            root.left = build(left, mapping[root.val] - 1, mapping, preorder, inorder)
            root.right = build(mapping[root.val] + 1, right, mapping, preorder, inorder)
            return root
        
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        return build(0, len(inorder) - 1, idx_map, preorder, inorder)
    
