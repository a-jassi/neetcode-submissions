class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None] * n

        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1 
            if cache[i]:
                return cache[i]
            
            cache[i] = dp(i + 1) + dp(i + 2)
            return cache[i]

        return dp(0)
            
