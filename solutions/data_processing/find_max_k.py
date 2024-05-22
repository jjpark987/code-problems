#!/usr/bin/env python3

# import ipdb
from typing import List
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # create set with the list elements
        nums_set = set(nums)

        # initialize max_value
        max_value = -1

        # iterate through set
        for n in nums_set:

            # look for their corresponding sign in set
            if -n in nums_set:
                # set max value to positive n if n is greater
                max_value = max(max_value, abs(n))

        # return the max value 
        return max_value

print(Solution().findMaxK([-1,2,-3,3]))
print(Solution().findMaxK([-1,10,6,7,-7,1]))
print(Solution().findMaxK([-10,8,6,7,-2,-3]))
