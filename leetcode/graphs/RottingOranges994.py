from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        time = 0

        ROW = len(grid)
        COL = len(grid[0])

        # add all rotten oranges to queue to start the rotting process
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    queue.append((i, j))

        firstIteration = True

        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                # go over neighbours
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        # skip self
                        if i == 0 and j == 0 or abs(i) == abs(j):
                            continue
                        # if valid neighbour
                        if ROW > r + i >= 0 and COL > c + j >= 0 and grid[r + i][c + j] == 1:
                            # mark as visited
                            grid[r + i][c + j] = 2
                            queue.append((r + i, c + j))
            # no need to increment time as first round or oranges are already rotten
            # we can start with adjacent oranges to the already rotten oranges but this solution is easier to write
            if not firstIteration:
                time += 1

            firstIteration = False

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    return -1
        return time