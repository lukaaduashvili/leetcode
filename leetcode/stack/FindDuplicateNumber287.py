from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        num = 0
        for i in range(len(nums)):
            if num & (1 << nums[i]):
                return nums[i]
            num = num | (1 << nums[i])
        return -1