class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        steps = []
        for i in range(n + 1):
            steps.append(0)

        steps[1] = 1
        steps[2] = 2
        self.helper(n, steps)
        return steps[n]

    def helper(self, n, steps):
        if steps[n] != 0:
            return steps[n]
        steps[n] = self.helper(n - 1, steps) + self.helper(n - 2, steps)
        return steps[n]