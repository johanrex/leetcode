# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        depth = 1
        nodes_on_level = [root]

        while True:
            if any(
                node
                for node in nodes_on_level
                if node.left is None and node.right is None
            ):
                break

            nodes_on_next_level = []
            for node in nodes_on_level:
                if node.left is not None:
                    nodes_on_next_level.append(node.left)
                if node.right is not None:
                    nodes_on_next_level.append(node.right)

            depth += 1
            nodes_on_level = nodes_on_next_level

        return depth
