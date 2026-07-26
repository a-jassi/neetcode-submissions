class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        res = math.inf
        curr = 0

        for r in range(len(nums)):
            curr += nums[r]

            while curr >= target:
                res = min(res, r - l + 1)
                curr -= nums[l]
                l += 1
            
        return 0 if res == math.inf else res
            