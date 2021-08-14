# RELATED TOPICS:
# Tree | Depth-First Search | Breadth-First Search | Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        subTreeRoots = {}
        seen = set()
        duplicates = set()
        
        def traverse(node):
            if not node:
                return 'e'
            left = traverse(node.left)
            right = traverse(node.right)
            cur = str(node.val) + 'l' + left + 'r' + right
            if cur not in seen:
                subTreeRoots[cur] = node
                seen.add(cur)
            else:
                duplicates.add(subTreeRoots[cur])
            return cur
        
        traverse(root)
        return list(duplicates)
    
