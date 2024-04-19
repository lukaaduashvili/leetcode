class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost_for_step = [-1 for i in range(len(cost))]

        def helper(n):
            if n == len(cost):
                return 0

            if min_cost_for_step[n] != -1:
                return min_cost_for_step[n]

            min_cost = 0
            if n == len(cost) - 1:
                min_cost = cost[n] + helper(n + 1)
            else:
                min_cost = cost[n] + min(helper(n + 1), helper(n + 2))
            min_cost_for_step[n] = min_cost

            return min_cost

        return min(helper(0), helper(1))