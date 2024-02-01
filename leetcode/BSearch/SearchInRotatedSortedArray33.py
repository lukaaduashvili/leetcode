from typing import List


def bSearch(nums, target, lo, hi):
    if lo == hi and nums[lo] == target: return 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            hi = mid - 1
        elif target > nums[mid]:
            lo = mid + 1
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 1, len(nums) - 1
        pivot = -1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[mid - 1]:
                pivot = mid
                break

            if nums[mid] > nums[0]:
                lo = mid + 1
            elif nums[mid] <= nums[0]:
                hi = mid

        if pivot == -1:
            if nums[0] < nums[-1]:
                pivot = 0
            else:
                pivot = len(nums) - 1

        if nums[pivot] == target:
            return pivot

        if pivot == 0:
            return bSearch(nums, target, 0, len(nums)-1)

        if nums[0] <= target <= nums[pivot-1]:
            return bSearch(nums, target, 0, pivot)
        elif nums[pivot] <= target <= nums[-1]:
            return bSearch(nums, target, pivot, len(nums) - 1)

        return -1




if __name__ == '__main__':
    s = Solution()
    print(s.search([5, 1, 3], 3))