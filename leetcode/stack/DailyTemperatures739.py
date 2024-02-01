from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i in range(len(temperatures)):
            res.append(0)
        stack.append((0, temperatures[0]))
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][1]:
                res[stack[-1][0]] = (i - stack[-1][0])
                stack.pop()

            stack.append((i, temperatures[i]))

        while not stack:
            res[stack.pop()[0]] = 0

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
