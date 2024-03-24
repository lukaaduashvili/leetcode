from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1+val2)
            elif op == "C":
                stack.pop()
            elif op == "D":
                val = stack.pop()
                stack.append(val*2)
            else:
                stack.append(op)

        val = 0
        for i in range(len(stack)):
            val += int(stack.pop())

        return val
