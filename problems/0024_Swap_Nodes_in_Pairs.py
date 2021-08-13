# RELATED TOPICS:
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        a = head
        b = a.next
        a.next = b.next
        b.next = a
        a.next = self.swapPairs(a.next)
        return b
    
