# RELATED TOPICS:
# Linked List | Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """# only swap nodes not values
        if not head.next:
            return head
        
        list_len = 0
        node = head
        while node:
            list_len += 1
            node = node.next
        if k == (list_len + 1) / 2:
            return head
        
        if k == 1 or k == list_len:
            node = head
            while node.next.next:
                node = node.next
            last = node.next
            if list_len == 2:
                last.next = head
                head.next = None
                return last
            last.next = head.next
            node.next = head
            head.next = None
            return last
        
        if k > list_len / 2:
            k = list_len - k + 1
        node1_pre = node2_pre = head
        for _ in range(2, k):
            node1_pre = node1_pre.next
        for _ in range(2, list_len - k + 1):
            node2_pre = node2_pre.next
        node1 = node1_pre.next
        if k == list_len / 2 or k == list_len / 2 + 1:
            node2 = node1.next
            node1.next = node2.next
            node1_pre.next = node2
            node2.next = node1
        else:
            node2 = node2_pre.next
            temp = ListNode(val=node1.val, next=node1.next)
            node1.next = node2.next
            node2_pre.next = node1
            node2.next = temp.next
            node1_pre.next = node2
        return head"""
        
        # swap values not nodes
        s = []
        cur = head
        while cur:
            s.append(cur)
            cur = cur.next
        s[k-1].val, s[-k].val = s[-k].val,s[k-1].val
        return head
    
