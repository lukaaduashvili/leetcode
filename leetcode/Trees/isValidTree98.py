# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.lst = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.lst.append(root.val)
            inorder(root.right)

        inorder(root)
        for i in range(1, len(self.lst)):
            if self.lst[i - 1] >= self.lst[i]:
                return False
        return True