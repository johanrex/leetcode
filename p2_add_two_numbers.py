# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        result_node_first = None
        result_node_prev = None

        carry = 0
        while True:
            if l1 is None and l2 is None and carry == 0:
                break

            l1val = l1.val if l1 is not None else 0
            l2val = l2.val if l2 is not None else 0

            total_sum = carry + l1val + l2val

            current_node_sum = total_sum % 10
            carry = total_sum // 10

            result_node_current = ListNode(current_node_sum)

            if result_node_prev == None:
                result_node_first = result_node_current
            else:
                result_node_prev.next = result_node_current

            result_node_prev = result_node_current

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return result_node_first


# l1n1 = ListNode(2, next=ListNode(4, next=ListNode(3, next=ListNode(9))))
# l2n1 = ListNode(5, next=ListNode(6, next=ListNode(4)))


def create_linked_list(arr):
    first_node = None
    prev_node = None
    for val in arr:
        current_node = ListNode(val)

        if prev_node is not None:
            prev_node.next = current_node

        prev_node = current_node
        if first_node is None:
            first_node = current_node

    return first_node


def print_linked_list(l):
    arr = []
    while True:
        arr.append(l.val)
        l = l.next
        if l is None:
            break
    print(arr)


l1 = create_linked_list([9, 9, 9, 9, 9, 9, 9])
l2 = create_linked_list([9, 9, 9, 9])

s = Solution()
l = s.addTwoNumbers(l1, l2)
print_linked_list(l)
