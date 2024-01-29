from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1
        if hi == 0 and nums[hi] == target:
            return 0
        while lo < hi:
            mid = lo + (hi - lo + 1) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid
        return -1
