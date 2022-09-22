class MinStack:
    
    def __init__(self):
        self.Stack = []

    def push(self, val: int) -> None:
        x = self.Stack
        x.append(val)
    def pop(self) -> None:
        x = self.Stack
        x.pop()
    def top(self) -> int:
        x = self.Stack[-1]
        return x

    def getMin(self) -> int:
        return min(self.Stack)
