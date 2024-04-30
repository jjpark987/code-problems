#!/usr/bin/env python

import ipdb
import functools

class Solution:
    def __init__(self):
        self.cache = {}

    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        self.cache[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

        return self.cache[n]
    
    # @functools.cache
    # def tribonacci(self, n: int) -> int:
    #     if n == 0:
    #         return 0
    #     elif n == 1 or n == 2:
    #         return 1

    #     return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            
print(Solution().tribonacci(n=40))