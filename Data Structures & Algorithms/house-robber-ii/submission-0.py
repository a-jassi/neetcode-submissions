class Solution:
    def rob(self, nums: List[int]) -> int:

        def dp(nums):
            rob1, rob2 = 0, 0

            for n in nums:
                newRob = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = newRob
            
            return rob2
        
        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))