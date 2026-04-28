class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        for i in range(1, len(nums)):
            prefixes[i] = nums[i-1] * prefixes[i-1]
        
        suffixes = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffixes[i] = nums[i+1] * suffixes[i+1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefixes[i] * suffixes[i]
        
        return res
