class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def rearrange_stacks(self) -> None:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.rearrange_stacks()
        return self.s2.pop()

    def peek(self) -> int:
        self.rearrange_stacks()
        return self.s2[-1]

    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0
