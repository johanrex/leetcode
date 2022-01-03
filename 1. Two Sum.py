"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

from typing import List


def sort_func(tup):
    return tup[0]


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        indexes = list(range(len(nums)))

        zipped = zip(nums, indexes)

        sorted_tuples = sorted(zipped, key=sort_func)

        idx_low = 0
        idx_high = len(nums) - 1

        # assume solution exists
        while True:

            val_low = sorted_tuples[idx_low][0]
            val_high = sorted_tuples[idx_high][0]

            sum = val_low + val_high

            if sum == target:
                break
            elif sum < target:
                idx_low += 1
            else:
                idx_high -= 1

        return [sorted_tuples[idx_low][1], sorted_tuples[idx_high][1]]


import random

nums = random.sample(range(-109, 109), 104)
target = nums[50] + nums[51]

print(f"target: {target}")

s = Solution()
ans = s.twoSum(nums, target)
print(ans)

print(f"gives {nums[ans[0]]+nums[ans[1]]}")
