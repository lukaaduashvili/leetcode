import heapq
from math import sqrt
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        nums = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            nums.append((sqrt(x * x + y * y), points[i]))

        heapq.heapify(nums)
        print(nums)

        ans = []
        while k > 0:
            ans.append(heapq.heappop(nums)[1])
            k -= 1
        return ans
