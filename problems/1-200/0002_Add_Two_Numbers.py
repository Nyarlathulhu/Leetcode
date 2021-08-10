# RELATED TOPICS:
# Linked List | Math | Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = []
        carry = 0
        while l1 and l2:
            cur_sum = l1.val + l2.val + carry
            if cur_sum >= 10:
                cur_sum -= 10
                carry = 1
            else:
                carry = 0
            ans.append(cur_sum)
            l1 = l1.next
            l2 = l2.next
        while l1:
            cur_num = l1.val + carry
            if cur_num >= 10:
                cur_num -= 10
                carry = 1
            else:
                carry = 0
            ans.append(cur_num)
            l1 = l1.next
        while l2:
            cur_num = l2.val + carry
            if cur_num >= 10:
                cur_num -= 10
                carry = 1
            else:
                carry = 0
            ans.append(cur_num)
            l2 = l2.next
        if carry and (not l1 and not l2):
            ans.append(1)
        ans_head = ListNode(val=ans[0])
        pre_node = ans_head
        for i in range(1, len(ans)):
            cur_node = ListNode(val=ans[i])
            pre_node.next = cur_node
            pre_node = cur_node
        return ans_head
    
