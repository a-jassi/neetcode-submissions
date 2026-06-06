class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, numOpen, numClose):
            if (numOpen == numClose) and len(curr) == (2 * n):
                res.append("".join(curr))
                return
            
            if numClose > numOpen or numOpen > n:
                return
            
            curr.append('(')
            backtrack(curr, numOpen + 1, numClose)
            curr.pop()

            curr.append(")")
            backtrack(curr, numOpen, numClose + 1)
            curr.pop()            

        backtrack([], 0, 0)
        return res