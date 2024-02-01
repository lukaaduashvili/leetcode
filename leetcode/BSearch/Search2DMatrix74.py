from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        lo, hi = 0, len(matrix) * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            r = mid // n
            c = mid % n
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                lo = mid+1
            elif matrix[r][c] > target:
                hi = mid - 1

        return False

