class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(currIndex, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return

            currDigit = digits[currIndex]
            for c in digitMap[currDigit]:
                backtrack(currIndex + 1, curr + c)
            
        if digits:
            backtrack(0, "")
        return res

            

