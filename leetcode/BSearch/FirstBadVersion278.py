
def isBadVersion(version: int) -> bool:
    return True
class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 2, n
        if n == 1 and isBadVersion(1):
            return 1
        elif n == 1:
            return -1

        while lo <= hi:
            mid = (lo + hi) // 2
            prev = mid - 1
            if isBadVersion(mid) and isBadVersion(prev):
                hi = mid - 1
            elif not isBadVersion(mid) and not isBadVersion(prev):
                lo = mid + 1
            elif isBadVersion(mid) and not isBadVersion(prev):
                return mid
