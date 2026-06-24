class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * len(cost)
        def dp(i):
            if i >= len(cost):
                return 0
            if cache[i] != -1:
                return cache[i]

            sum = cost[i] + min(dp(i+1), dp(i+2))
            cache[i] = sum
            return sum
        
        return min(dp(0), dp(1))
