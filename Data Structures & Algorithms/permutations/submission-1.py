class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr, seen):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(seen)):
                if not seen[i]:
                    curr.append(nums[i])
                    seen[i] = True
                    backtrack(curr, seen)
                    curr.pop()
                    seen[i] = False
        
        backtrack([], [False for _ in nums])
        return res
