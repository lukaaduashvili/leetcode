# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.pspsps = 0
        self.cnt = k

        def inorder(tree):
            if not tree or self.cnt < 1:
                return
            inorder(tree.left)
            self.cnt -= 1
            if self.cnt == 0:
                self.pspsps = tree.val
                return
            inorder(tree.right)

        inorder(root)
        return self.pspsps