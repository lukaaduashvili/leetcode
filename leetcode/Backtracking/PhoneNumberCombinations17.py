class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def getLetter(digit):
            phone_map = [
                'abc',
                'def',
                'ghi',
                'jkl',
                'mno',
                'pqrs',
                'tuv',
                'wxyz']
            return phone_map[digit - 2]

        self.res = []

        def helper(lst, digits, idx):
            if idx == len(digits):
                self.res.append("".join(lst))
                return
            for curr in getLetter(int(digits[idx])):
                lst.append(curr)
                helper(lst, digits, idx + 1)
                lst.pop()

        if digits == "":
            return self.res
        helper([], digits, 0)
        return self.res
