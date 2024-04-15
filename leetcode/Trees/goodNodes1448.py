# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.numNodes = 0

        def helper(root, max_n):
            if root is None:
                return

            old_max = max_n

            if root.val >= max_n:
                max_n = root.val
                self.numNodes += 1

            helper(root.left, max_n)
            helper(root.right, max_n)

        helper(root, float('-inf'))
        return self.numNodes