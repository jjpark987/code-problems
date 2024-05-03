#!/usr/bin/env python3

# import ipdb
# from typing import List
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # extract the revisions for both versions in lists
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))

        # make the two lists equal if not already
        while len(v1) < len(v2):
            v1.append(0)
        while len(v1) > len(v2):
            v2.append(0)
        
        # iterate using range
        for i in range(len(v1)):
            # compare elements in v1, v2 and return appropriate output if not equal
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
            
        return 0

print(Solution().compareVersion('1.01', '1.001.00'))