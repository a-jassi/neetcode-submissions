class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, currArr, currSum):
            if currSum == target:
                res.append(currArr.copy())
                return
            if currSum > target or i >= len(candidates):
                return
            
            currArr.append(candidates[i])
            backtrack(i + 1, currArr, currSum + candidates[i])
            currArr.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, currArr, currSum)
        
        backtrack(0, [], 0)
        return res
            