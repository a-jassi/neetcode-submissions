class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, currArr, currSum):
            if currSum == target:
                res.append(currArr[:])
                return
            if currSum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                                  
                currArr.append(candidates[i])
                currSum += candidates[i]

                backtrack(i+1, currArr, currSum)

                num = currArr.pop()
                currSum -= num
        
        backtrack(0, [], 0)
        return res