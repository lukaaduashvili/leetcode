class MyStack:

    def __init__(self):
        self.main = []
        self.supp = []
    def push(self, x: int) -> None:
        self.main.append(x)
    def pop(self) -> int:
        while len(self.main) > 1:
            self.supp.append(self.main.pop(0))

        last_num = self.main.pop(0)

        while self.supp:
            self.main.append(self.supp.pop(0))

        return last_num
    def top(self) -> int:
        while len(self.main) > 1:
            self.supp.append(self.main.pop(0))

        last_num = self.main.pop(0)
        self.supp.append(last_num)

        while self.supp:
            self.main.append(self.supp.pop(0))

        return last_num
    def empty(self) -> bool:
        return len(self.main) == 0