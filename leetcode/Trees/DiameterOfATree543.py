# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def helper(root):
            if not root:
                return 0

            left = helper(root.left)
            right = helper(root.right)

            if (left + right) > self.max:
                self.max = left + right

            return 1 + max(left, right)

        helper(root)

        return self.max