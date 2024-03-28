class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        minim = self.getMin()
        if self.getMin() is None:
            minim = val
        elif val <= self.getMin():
            minim = val

        self.stack.append(val)
        self.minStack.append(minim)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return None
        return self.minStack[-1]
