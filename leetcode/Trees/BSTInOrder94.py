# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lits = []
        def traverse(tree):
            if not tree:
                return
            traverse(tree.left)
            lits.append(tree.val)
            traverse(tree.right)
        traverse(root)
        return lits