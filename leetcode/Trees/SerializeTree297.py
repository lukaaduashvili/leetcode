# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        temp = []

        def dfs(root):
            if not root:
                temp.append("null")
                return
            temp.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return ",".join(temp)

    def deserialize(self, data):
        self.val = data.split(",")
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.idx = 0

        def dfs():
            if self.val[self.idx] == 'null':
                self.idx += 1
                return None

            root = TreeNode(self.val[self.idx])
            self.idx += 1

            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))