# RELATED TOPICS:
# Array | Linked List | Stack | Monotonic Stack

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        answer = [0] * 10000
        mono_stack = deque()
        mono_stack.append([1, head.val])
        cur = head
        i = 2
        while cur.next:
            if cur.next.val <= cur.val:
                mono_stack.append([i, cur.next.val])
            else:
                pops = []
                while mono_stack and mono_stack[-1][1] < cur.next.val:
                    answer[mono_stack.pop()[0]-1] = cur.next.val
                mono_stack.append([i, cur.next.val])
            cur = cur.next
            i += 1
        return answer[:i-1]
        
