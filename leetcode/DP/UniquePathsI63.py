class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        prevRow = [0] * n
        prevRow[n - 1] = 1
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        for i in range(m - 1, -1, -1):
            curr_row = [0] * n
            if obstacleGrid[i][n - 1] == 0 and prevRow[n-1] != 0:
                curr_row[n - 1] = 1

            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] == 0:
                    curr_row[j] = curr_row[j+1] + prevRow[j]
                else:
                    curr_row[j] = 0
            prevRow = curr_row
        return prevRow[0]