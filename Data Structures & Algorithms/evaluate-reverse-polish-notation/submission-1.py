class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def rpn():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)
            
            right = rpn()
            left = rpn()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            else:
                return int(left / right)
        
        return rpn()