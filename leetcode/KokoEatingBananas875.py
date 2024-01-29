import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 2, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.isEdible(piles, h, mid) and not self.isEdible(piles, h, mid-1):
                return mid
            elif not self.isEdible(piles, h, mid) and not self.isEdible(piles, h, mid-1):
                lo = mid + 1
            elif self.isEdible(piles, h, mid) and self.isEdible(piles, h, mid-1):
                hi = mid - 1

        return -1


    def isEdible(self, piles: List[int], h: int, k: int) -> bool:
        sumH = 0
        for i in range(len(piles)):
            sumH += math.ceil(piles[i] / k)

        return sumH <= h
