"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. 
Answers within 10**-5 of the actual answer will be accepted. 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
from typing import List, Optional


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # BFS
        result = []

        q = deque()
        q.append(root)

        while len(q) > 0:
            nr_of_nodes_on_level = len(q)
            sum_of_level = 0

            i = nr_of_nodes_on_level
            while i > 0:
                i -= 1

                v = q.popleft()
                sum_of_level += v.val

                if v.left:
                    q.append(v.left)

                if v.right:
                    q.append(v.right)

            result.append(sum_of_level / nr_of_nodes_on_level)
        return result
