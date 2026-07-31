class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(curr, left, right):
            if left == right == n:
                res.append("".join(curr))
                return
            
            if left > n or right > n or right > left:
                return
            
            curr.append('(')
            backtrack(curr, left + 1, right)
            curr.pop()
            curr.append(')')
            backtrack(curr, left, right + 1)
            curr.pop()
        
        backtrack([], 0, 0)
        return res