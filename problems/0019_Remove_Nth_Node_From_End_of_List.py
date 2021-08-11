# RELATED TOPICS:
# Linked List | Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        left = start
        right = head
        while right:
            if n <= 0:
                left = left.next
            right = right.next
            n -= 1
        left.next = left.next.next
        return start.next
    
