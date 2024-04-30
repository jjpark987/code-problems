#!/usr/bin/env python

import ipdb
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        elif n == 2:
            return [0, 1]

        adj_list = {i: [] for i in range(n)}

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        leaves = {node for node in adj_list if len(adj_list[node]) == 1}

        while n > 2:
            n -= len(leaves)
            new_leaves = set()

            for node in leaves:
                neighbor = adj_list[node].pop()
                adj_list[neighbor].remove(node)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.add(neighbor)

            leaves = new_leaves

        return list(new_leaves)
            
print(Solution().findMinHeightTrees(n=4, edges=[[1,0],[1,2],[1,3]]))
print(Solution().findMinHeightTrees(n=6, edges=[[3,0],[3,1],[3,2],[3,4],[5,4]]))
print(Solution().findMinHeightTrees(n=6, edges=[[0,1],[0,2],[0,3],[3,4],[4,5]]))