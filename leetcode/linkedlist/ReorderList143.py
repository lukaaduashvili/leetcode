# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        while curr:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n

        slow.next = None

        slow_half = head
        fast_half = prev

        while slow_half:
            temp1 = slow_half.next
            temp2 = fast_half.next

            fast_half.next = temp1
            slow_half.next = temp2

            fast_half = temp2
            slow_half = temp1


if __name__ == "__main__":
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution.reorderList(head)
