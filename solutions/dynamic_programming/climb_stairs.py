#!/usr/bin/env python

# import ipdb
# from typing import List
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}

        def climb(n):
            if n in cache:
                return cache[n]

            if n == 0 or n == 1:
                return 1
            
            cache[n] = climb(n - 1) + climb(n - 2)
            
            return cache[n]
        
        return climb(n)
    
        # if n == 0 or n == 1:
        #     return 1
        
        # prev, curr = 1, 1

        # for i in range(2, n+1):
        #     temp = curr
        #     curr = prev + curr
        #     prev = temp
        
        # return curr

print(Solution().climbStairs(n=2))
print(Solution().climbStairs(n=3))
print(Solution().climbStairs(n=5))
