# RELATED TOPICS:
# String | Tree | Depth-First Search | Breadth-First Search | Design | Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        return f'{root.val} {self.serialize(root.left)} {self.serialize(root.right)}'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def buildTree(sequence):
            val = sequence.pop()
            if not val:
                return None
            node = TreeNode(val)
            node.left = buildTree(sequence)
            node.right = buildTree(sequence)
            return node
        
        if not data:
            return None
        return buildTree(list(reversed(data.split(' '))))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
