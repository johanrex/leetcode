"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:

    0 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""

from typing import List
import random


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []

        nums.sort()
        length = len(nums)

        for i in range(length):

            j = i + 1
            k = length - 1

            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                if sum == 0:
                    triple = [nums[i], nums[j], nums[k]]
                    if not triple in ans:
                        ans.append(triple)
                    j += 1
                elif sum < 0:
                    j += 1
                elif sum > 0:
                    k -= 1

        return ans


s = Solution()
print(s.threeSum([-2, 0, 1, 1, 2]))

print(s.threeSum([-1, 0, 1, 2, -1, -4]))
print(s.threeSum([]))
print(s.threeSum([0]))

nums = []
for _ in range(100):
    nums.append(random.randint(-105, 105))

print(s.threeSum(nums))
