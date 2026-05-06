class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.minStack.append(val)
        else:
            prevMin = self.minStack[-1]
            if val < prevMin:
                self.minStack.append(val)
            else:
                self.minStack.append(prevMin)
        
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
