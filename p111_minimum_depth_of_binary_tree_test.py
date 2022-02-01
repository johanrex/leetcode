from typing import List
from p111_minimum_depth_of_binary_tree import *


def test():

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    depth = s.minDepth(root)
    assert depth == 2


test()
