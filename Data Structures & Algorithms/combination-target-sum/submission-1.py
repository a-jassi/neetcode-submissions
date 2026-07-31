class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currSum, currArr):
            if currSum == target:
                res.append(currArr.copy())
                return
            if currSum > target or i >= len(nums):
                return
            
            currArr.append(nums[i])
            backtrack(i, currSum + nums[i], currArr)
            currArr.pop()
            backtrack(i + 1, currSum, currArr)
        
        backtrack(0, 0, [])
        return res