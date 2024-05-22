#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        curr, prev.next = prev.next, None
        while curr:
            temp = curr.next
            if curr.val >= prev.val:
                curr.next = prev
                prev = curr
            curr = temp

        return prev

test = ListNode(5)
test.next = ListNode(2)
test.next.next = ListNode(13)
test.next.next.next = ListNode(3)
test.next.next.next.next = ListNode(8)

print(Solution().removeNodes(head=test))
print('Expected output: [13,8]')