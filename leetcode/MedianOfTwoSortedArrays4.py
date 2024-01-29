from typing import List


class Solution:
    # O(N+M) solution not optimal
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_list = []
        i, j = 0, 0
        while True:
            if i >= len(nums1) and j < len(nums2):
                for j2 in range(j, len(nums2)):
                    merged_list.append(nums2[j2])
                break

            if j >= len(nums2) and i < len(nums1):
                for i2 in range(i, len(nums1)):
                    merged_list.append(nums1[i2])
                break

            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
            else:
                merged_list.append(nums2[j])
                j += 1

        if len(merged_list) % 2 == 1:
            return merged_list[len(merged_list) // 2]
        else:
            mid = len(merged_list) // 2
            mid2 = mid - 1
            return (merged_list[mid] + merged_list[mid2]) / 2.0

if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1, 2], [3, 4]))
