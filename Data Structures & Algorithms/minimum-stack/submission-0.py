class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')
        self.d = {-1: float('inf')}

    def push(self, val: int) -> None:
        self.d[len(self.stack)] = min(val, self.d[len(self.stack)-1])       
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        del self.d[len(self.stack)]      

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.d[len(self.stack) - 1]
