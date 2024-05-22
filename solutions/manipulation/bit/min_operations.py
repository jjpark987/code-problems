#!/usr/bin/env python

import ipdb
from typing import List
from functools import reduce
# from collections import deque

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = reduce(lambda x, y: x ^ y, nums)
        moves = 0

        while k or xor:
            if k % 2 != xor % 2:
                moves += 1
        
            k //= 2
            xor //= 2

        return moves

print(Solution().minOperations(nums=[2,1,3,4], k=1))
