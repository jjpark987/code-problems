#!/usr/bin/env python

import ipdb
# from typing import List
# from functools import reduce
from collections import deque, defaultdict

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        stack = deque()
        result = ''

        for i, char in enumerate(word):
            stack.append(char)

            if char == ch:
                for _ in range(len(stack)):
                    result += stack.pop()
                
                result += word[i + 1:]

                break
        
        return result
    
        # i = word.find(ch)
        # if i != -1:
        #     return word[:i+1][::-1] + word[i+1:]
        # return word

print(Solution().reversePrefix(word = 'abcdefd', ch = 'd'))
