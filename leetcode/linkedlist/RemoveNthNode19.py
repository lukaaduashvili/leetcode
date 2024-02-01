# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if n == size:
            return head.next

        curr = head
        for i in range(size - n - 1):
            curr = curr.next
        next_n = curr.next.next
        curr.next = next_n

        return head


if __name__ == '__main__':
    s = Solution()
    lst = ListNode(1)
    lst.next = ListNode(2)
    lst.next.next = ListNode(3)
    lst.next.next.next = ListNode(4)
    lst.next.next.next.next = ListNode(5)
    s.removeNthFromEnd(lst, 5)