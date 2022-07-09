# RELATED TOPICS
# Linked List | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        node1 = list1
        node2 = list2
        
        while node1 and node2:
            if node1.val < node2.val:
                cur.next = node1
                cur = node1
                node1 = node1.next
            else:
                cur.next = node2
                cur = node2
                node2 = node2.next
        
        if node1 or node2:
            cur.next = node1 if node1 else node2
        
        return head.next
    
