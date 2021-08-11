# RELATED TOPICS:
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def swap(node):
            if not node:
                return None
            if not node.next:
                return node
            a = node
            b = a.next
            a.next = b.next
            b.next = a
            a.next = swap(a.next)
            return b
        
        return swap(head)
    
