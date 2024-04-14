# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        sum = 0

        def helper(root, targetSum, sum):
            if not root:
                return False

            sum += root.val

            if not root.left and not root.right and sum == targetSum:
                return True

            if helper(root.left, targetSum, sum):
                return True

            if helper(root.right, targetSum, sum):
                return True

            sum -= root.val

            return False

        return helper(root, targetSum, sum)