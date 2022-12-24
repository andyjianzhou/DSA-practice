# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lp, rp = 0, n
        while lp <= rp:
            mid = (lp + rp) // 2
            bad = isBadVersion(mid)
            if bad == True:
                return mid
            else:
                rp = mid - 1
                lp = mid + 1
            
            