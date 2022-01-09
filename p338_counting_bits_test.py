from p338_counting_bits import *


def test():

    s = Solution()

    assert [0, 1, 1] == s.countBits(2)
    assert [0, 1, 1, 2, 1, 2] == s.countBits(5)
    assert [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2] == s.countBits(10)


test()
