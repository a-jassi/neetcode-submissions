class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(curr, seen):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not seen[i-1]:
                    continue

                if not seen[i]:
                    seen[i] = True
                    curr.append(nums[i])
                    backtrack(curr, seen)
                    seen[i] = False
                    curr.pop()
                
            
        backtrack([], [False for _ in nums])
        return res
            
