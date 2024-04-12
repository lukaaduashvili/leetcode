from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elems = {}
        for num in nums:
            if num in elems:
                elems[num] += 1
            else:
                elems[num] = 1

        majority = len(nums) // 2 + 1
        for num, cnt in elems.items():
            if cnt > majority:
                return num
        return -1