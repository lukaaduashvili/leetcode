from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                node = self.findMin(root.right)
                root.val = node.val
                root.right = self.deleteNode(root.right, root.val)
        return root

    def findMin(self, tree):
        while tree and tree.left:
            tree = tree.left
        return tree
