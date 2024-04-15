# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0

            left = height(root.left)
            right = height(root.right)

            return 1 + max(left, right)

        def helper(root):
            if root is None:
                return True

            n = height(root.left) - height(root.right)

            if abs(n) > 1:
                return False

            return helper(root.left) and helper(root.right)

        return helper(root)


