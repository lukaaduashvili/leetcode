# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(a, b):
            if not a and not b:
                return True
            elif not a or not b:
                return False

            return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

        def helper(root, subRoot):
            if root is None and subRoot is not None:
                return False

            if isSameTree(root, subRoot):
                return True

            return helper(root.left, subRoot) or helper(root.right, subRoot)

        helper(root, subRoot)

        return helper(root, subRoot)
