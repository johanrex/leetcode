"""
https://leetcode.com/problems/counting-bits/

Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
    0 <= n <= 105

"""
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [None] * (n + 1)

        for i in range(n + 1):
            ans[i] = bin(i).count("1")

        return ans


s = Solution()
print(s.countBits(2))
print(s.countBits(5))
print(s.countBits(10))
