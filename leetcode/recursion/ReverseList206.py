# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head

        next_n = head.next
        head.next = None

        return self.helper(next_n, head)

    def helper(self, curr, prev):
        if curr is None:
            return prev

        next_n = curr.next
        curr.next = prev
        prev = curr
        curr = next_n

        return self.helper(curr, prev)

if __name__ == '__main__':
    print(ord('a'))