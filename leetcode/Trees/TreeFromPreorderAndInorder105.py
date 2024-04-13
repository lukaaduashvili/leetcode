# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        # left preorder is from 1st index to indexOf current node in inorder
        # left inorder is from 0 to indexOf currentNode not inclusive
        root.left = self.buildTree(preorder[1:mid + 1], inorder[0:mid])
        # right subtree is built from remaining arrays

        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root