# RELATED TOPICS:
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        # iteratively
        if not head:
            return None
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
        def reverse(node):
            if not node:
                return None
            if not node.next:
                return node
            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last
        
        return reverse(head)
    
