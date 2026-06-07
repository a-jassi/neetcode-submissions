class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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
                res.append("".join(curr))
                return

            currDigit = digits[currIndex]
            for c in digitMap[currDigit]:
                curr.append(c)
                backtrack(currIndex + 1, curr)
                curr.pop()
            
        backtrack(0, [])
        return res

            

