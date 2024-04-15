# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max = float("-inf")
        def helper(root):
            if not root:
                return 0

            left = max(0, helper(root.left))
            right = max(0, helper(root.right))

            if root.val + left + right > self.max:
                self.max = root.val + left + right

            return root.val + max(left, right)

        helper(root)

        return self.max