from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev = head
        head = head.next
        prev.next = None
        while head is not None:
            next_n = head.next
            head.next = prev
            prev = head
            head = next_n
        return prev
