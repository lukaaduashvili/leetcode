import copy
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque()
        if root:
            queue.append(root)

        while len(queue) > 0:
            temp_q = copy.copy(queue)
            temp_q.popleft()
            for i in range(len(queue)):
                curr = queue.popleft()
                next_n = None
                if len(temp_q) > 0:
                    next_n = temp_q.popleft()
                curr.next = next_n
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return root
