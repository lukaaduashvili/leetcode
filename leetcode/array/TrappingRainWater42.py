from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_h = []
        right_h = []
        length = len(height)
        for i in range(length):
            left_h.append(0)
            right_h.append(0)
        left = 0
        right = 0
        for i in range(length):
            if height[i] > left:
                left = height[i]

            if height[length - i - 1] > right:
                right = height[length - i - 1]

            left_h[i] = left
            right_h[length - i - 1] = right

        water_sum = 0
        for i in range(length):
            water_sum += min(left_h[i], right_h[i]) - height[i]

        return water_sum


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))