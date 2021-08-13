# RELATED TOPICS:
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        """
        # iteratively
        pre = head
        cur = pre.next
        while cur:
            if pre == head:
                pre.next = None
            temp = cur
            cur = cur.next
            temp.next = pre
            pre = temp
        return pre
        """
        
        # recursively
        if not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
        
