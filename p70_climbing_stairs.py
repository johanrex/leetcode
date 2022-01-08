"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""


class Solution:
    def __init__(self) -> None:
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        else:
            tmp = n - 2
            if tmp in self.memo:
                climb_n_2 = self.memo[tmp]
            else:
                climb_n_2 = self.climbStairs(tmp)
                self.memo[tmp] = climb_n_2

            tmp = n - 1
            if tmp in self.memo:
                climb_n_1 = self.memo[tmp]
            else:
                climb_n_1 = self.climbStairs(tmp)
                self.memo[tmp] = climb_n_1

            return climb_n_1 + climb_n_2


s = Solution()

assert 2 == s.climbStairs(2)
assert 3 == s.climbStairs(3)
assert 63245986 == s.climbStairs(38)

print("Done")
