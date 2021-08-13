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
        
        if left == 1:
            first, _ = reverseFirstN(head, right)
            return first
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
        
