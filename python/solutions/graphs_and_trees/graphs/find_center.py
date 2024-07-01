#!/usr/bin/env python3

from typing import List, Optional
# from collections import Counter, deque, defaultdict
# from functools import reduce

# time: O(1), space: O(1)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0][0]
        y = edges[0][1]

        for edge in edges[1]:
            if edge == x:
                return x
            if edge == y:
                return y

print(Solution().findCenter([[1,2],[2,3],[4,2]]))
print('Expected: 2')
print(Solution().findCenter([[1,2],[5,1],[1,3],[1,4]]))
print('Expected: 1')

"""
EASY

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

Example 1:
/python/images/find_center_e1.png

Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
Example 2:

Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
 

Constraints:

3 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
The given edges represent a valid star graph.
"""