from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[0]:
                lo = mid
            elif nums[mid] <= nums[0]:
                hi = mid

        return min(nums[-1], nums[0])


if __name__ == '__main__':
    s = Solution()
    print(s.findMin([4, 1, 2]))
