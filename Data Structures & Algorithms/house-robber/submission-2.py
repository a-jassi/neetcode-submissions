class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        
        def dp(i):
            if i >= len(nums):
                return 0
            if cache[i] != -1:
                return cache[i]
            
            res = max(dp(i+1), nums[i] + dp(i+2))
            cache[i] = res
            return res
        
        return dp(0)