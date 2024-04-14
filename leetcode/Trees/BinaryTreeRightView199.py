# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        queue = deque()
        if root:
            queue.append(root)

        while len(queue) > 0:
            is_first = True
            for i in range(len(queue)):
                curr = queue.popleft()
                if is_first:
                    lst.append(curr.val)
                    is_first = False
                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
        return lst