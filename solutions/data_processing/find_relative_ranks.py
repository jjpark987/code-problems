#!/usr/bin/env python3

import ipdb
from typing import List, Optional
# from functools import reduce
# from collections import deque, defaultdict

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        medals = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        rank_map = {s: medals[i] if i < 3 else str(i + 1) for i, s in enumerate(sorted_score)}
        # for i, s in enumerate(sorted_score):
        #     match i:
        #         case 0:
        #             rank_map[s] = 'Gold Medal'
        #         case 1:
        #             rank_map[s] = 'Silver Medal'
        #         case 2:
        #             rank_map[s] = 'Bronze Medal'
        #         case _:
        #             rank_map[s] = str(i + 1)

        result = [rank_map[score[i]] for i in range(len(score))]

        return result
    

print(Solution().findRelativeRanks([10,3,8,9,4]))