from p637_average_of_levels_in_binary_tree import *


def test():
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)

    s = Solution()
    result = s.averageOfLevels(root)

    assert result == [1.0, 2.5, 5.0]


test()
