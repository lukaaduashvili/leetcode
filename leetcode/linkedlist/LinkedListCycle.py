from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        list_of_nodes = set()
        while head is not None:
            if head in list_of_nodes:
                return True
            list_of_nodes.add(head)
            head = head.next

        return False
