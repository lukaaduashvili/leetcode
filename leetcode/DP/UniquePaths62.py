class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [0] * n
        for i in range(m - 1, -1, -1):
            curr_row = [0] * n
            curr_row[n - 1] = 1
            for j in range(n - 2, -1, -1):
                curr_row[j] = curr_row[j+1] + prevRow[j]
            prevRow = curr_row
        return prevRow[0]