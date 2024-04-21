"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        queue = deque()
        queue.append(node)

        visited = {node.val: Node(node.val)}
        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                clone = visited[curr.val]

                for neighbour in curr.neighbors:
                    if neighbour.val not in visited:
                        queue.append(neighbour)
                        visited[neighbour.val] = Node(neighbour.val)
                    clone.neighbors.append(visited[neighbour.val])

        return visited[node.val]
