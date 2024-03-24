from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                unique += 1
                nums[unique] = nums[i]
        return unique