class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.visited = []
        for r in range(len(grid)):
            row = []
            for c in range(len(grid[0])):
                row.append(False)
            self.visited.append(row)

        def DFS(grid, r, c):
            if r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or r < 0 or c < 0 or self.visited[r][c]:
                return
            self.visited[r][c] = True
            DFS(grid, r + 1, c)
            DFS(grid, r - 1, c)
            DFS(grid, r, c + 1)
            DFS(grid, r, c - 1)

        numIslands = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if not self.visited[r][c] and grid[r][c] != "0":
                    DFS(grid, r, c)
                    numIslands += 1
        return numIslands