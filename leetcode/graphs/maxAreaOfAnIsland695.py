class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.visited = []
        for r in range(len(grid)):
            row = []
            for c in range(len(grid[0])):
                row.append(False)
            self.visited.append(row)

        def DFS(grid, r, c, size):
            if r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or r < 0 or c < 0 or self.visited[r][c]:
                return size
            self.visited[r][c] = True
            self.size += 1
            DFS(grid, r + 1, c, size + 1)
            DFS(grid, r - 1, c, size + 1)
            DFS(grid, r, c + 1, size + 1)
            DFS(grid, r, c - 1, size + 1)
            return size

        maxSize = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not self.visited[r][c] and grid[r][c] != 0:
                    self.size = 0
                    DFS(grid, r, c, 0)
                    maxSize = max(self.size, maxSize)
        return maxSize
