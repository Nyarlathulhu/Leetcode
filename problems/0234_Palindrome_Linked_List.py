# RELATED TOPICS:
# Linked List | Two Pointers | Stack | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            """
            reverse a linked list with head node
            """
            pre = None
            cur = node
            while cur:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            return pre
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        left = head
        right = reverse(slow)
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
