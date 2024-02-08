# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def traverse(new_root_new):
            if val > new_root_new.val:
                if new_root_new.right is None:
                    new_root_new.right = TreeNode(val)
                    return

                self.insertIntoBST(new_root_new.right, val)
            else:
                if new_root_new.left is None:
                    new_root_new.left = TreeNode(val)
                    return
                self.insertIntoBST(new_root_new.left, val)

        new_root = root
        traverse(new_root)
        return root

if __name__ == '__main__':
    s = Solution()
    s.insertIntoBST(None, 5)