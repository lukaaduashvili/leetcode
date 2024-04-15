from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        def generate(n, left, right, lst):
            if left==right==n:
                self.res.append("".join(lst))
                return
            if left < n:
                lst.append("(")
                generate(n, left + 1, right, lst)
                lst.pop()
            if right < left:
                lst.append(")")
                generate(n, left, right + 1, lst)
                lst.pop()

        generate(n, 0, 0, [])
        return self.res