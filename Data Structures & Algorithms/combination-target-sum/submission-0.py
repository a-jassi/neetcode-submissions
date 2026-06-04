class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start, currArr, currSum):
            if currSum == target:
                res.append(currArr[:])
                return
            if currSum > target:
                return
            
            for i in range(start, len(nums)):
                currArr.append(nums[i])
                currSum += nums[i]

                backtrack(i, currArr, currSum)

                num = currArr.pop()
                currSum -= num
        
        backtrack(0, [], 0)
        return res

                