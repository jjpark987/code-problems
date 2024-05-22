import ipdb
from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # bfs
        deadends = set(deadends)
        visted = set('0000')
        queue = deque([('0000', 0)])

        if '0000' in deadends:
            return -1

        while queue:
            current_combination, moves = queue.popleft()

            if current_combination == target:
                return moves
            
            for i in range(4):
                for delta in [-1, 1]:
                    new_digit = (int(current_combination[i]) + delta) % 10
                    new_combination = (
                        current_combination[:i] + str(new_digit) + current_combination[i+1:]
                    )

                    if new_combination not in deadends and new_combination not in visted:
                        visted.add(new_combination)
                        queue.append((new_combination, moves + 1))

        return -1
            
            
print(Solution().openLock(deadends=["0201","0101","0102","1212","2002"], target="0202"))