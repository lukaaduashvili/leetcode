class Solution:
    def guess(self, n: int) -> int:
        if n == 6:
            return 0
        if n < 6:
            return 1
        if n > 6:
            return -1

    def guessNumber(self, n: int) -> int:
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.guess(mid) == 0:
                return mid
            elif self.guess(mid) == 1:
                lo = mid
            elif self.guess(mid) == -1:
                hi = mid

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(10))