# RELATED TOPICS:
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseInterval(a, b):
            """
            reverse nodes from a to b, excluding b, [a, b)
            """
            pre = None
            cur = nxt = a
            while cur != b:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        a = b = head
        for _ in range(k):
            if b == None:
                return node
            b = b.next
        next_head = reverseInterval(a, b)
        a.next = self.reverseKGroup(b, k)
        return next_head
        
