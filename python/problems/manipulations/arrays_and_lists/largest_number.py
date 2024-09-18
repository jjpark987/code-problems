#!/usr/bin/env python3

from typing import List

# time: O(n*log(n)), space: O(n)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key=lambda x: int(x[0]), reverse= True)

        result = ''
        
        for n in nums:
            result += str(n)

        return result

print(Solution().largestNumber(nums = [10,2]))
print('210')
print(Solution().largestNumber(nums = [3,30,34,5,9]))
print('9534330')

"""
category: manipulations
subcategory: arrays_and_lists
difficulty: medium
image_url_e1: none
image_url_e2: none
image_url_e3: none
title: Largest Number

description:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""