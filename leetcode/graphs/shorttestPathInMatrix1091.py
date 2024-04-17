from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        length = 0
        ROW = len(grid)
        COL = len(grid[0])

        if grid[0][0] == 1:
            return -1

        queue.append((0, 0))

        while len(queue) > 0:
            length += 1
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length

                # go over neighbours
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # skip self
                        if i == 0 and j == 0:
                            continue
                        # if valid neighbour
                        if ROW > r + i >= 0 and COL > c + j >= 0 and grid[r + i][c + j] == 0:
                            # mark as visited
                            grid[r + i][c + j] = 1
                            queue.append((r + i, c + j))

        return -1
