# RELATED TOPICS:
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseFirstN(node, n):
            """
            reverse first N nodes of the linked list
            """
            if n == 1:
                successor = node.next
                return node, successor
            last, successor = reverseFirstN(node.next, n - 1)
            node.next.next = node
            node.next = successor
            return last, successor
        
        def reverse(node, m, n):
            """
            do as the problem requires
            """
            if m == 1:
                first, _ = reverseFirstN(node, n)
                return first
            node.next = reverse(node.next, m - 1, n - 1)
            return node
        
        return reverse(head, left, right)
    
