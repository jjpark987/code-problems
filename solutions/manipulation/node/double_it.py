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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go through list, doubling each node and handling carry
        prev, curr, carry, new_head = None, head, 0, None
        
        while curr:
            result = curr.val * 2 + carry
            curr.val = result % 10
            carry = result // 10

            if carry > 0 and prev == None:
                new_head = ListNode(carry)
                new_head.next = curr
                carry = 0
            elif carry > 0:
                prev.val += carry
                carry = 0

            prev, curr = curr, curr.next
        
        return new_head or head

        # # helper function to reverse linked list
        # def reverse_list(prev, curr):
        #     curr.next, prev, curr = prev, curr, curr.next
        #     return prev, curr

        # # helper function to double values and return carry
        # def double_node(node, carry) -> int:
        #     result = node.val * 2 + carry
        #     node.val = result % 10
        #     return result // 10

        # # reverse head as prev
        # prev, curr = None, head
        # while curr:
        #     prev, curr = reverse_list(prev, curr)

        # # change node value and save carry
        # carry = double_node(prev, 0)

        # # go through the list, changing its values and reversing its direction
        # curr, prev.next = prev.next, None
        # while curr:
        #     carry = double_node(curr, carry)
        #     prev, curr = reverse_list(prev, curr)

        # # create new node if carry is not zero
        # if carry:
        #     new_head, new_head.next = ListNode(carry), prev
        #     return new_head
        
        # return prev

test = ListNode(9)
test.next = ListNode(9)
test.next.next = ListNode(9)

print(Solution().doubleIt(head=test))
print('Expected output: [1, 9, 9, 8]')