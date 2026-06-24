class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dp(curr):
            if curr > n:
                return 0
            if curr == n:
                return 1
            if cache[curr] != -1:
                return cache[curr]

            sum = dp(curr + 1) + dp(curr + 2)
            cache[curr] = sum
            return sum
        
        return dp(0)
