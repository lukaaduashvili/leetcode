import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)

        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, x - y)

        if len(heap) == 1:
            return -1 * heap[0]
        return 0