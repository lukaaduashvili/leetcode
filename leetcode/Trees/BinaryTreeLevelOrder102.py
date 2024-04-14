# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        queue = deque()

        if root:
            queue.append(root)

        while len(queue) > 0:
            sublst = []
            for i in range(len(queue)):
                curr = queue.popleft()
                sublst.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            lst.append(sublst)

        return lst