# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # [1,2,3,4,5,6,7,8,9,10]
        # nums = [i for i in range(1,n+1)]
        # lp, rp = 0, len(nums)-1
        lp, rp = 1, n
        while lp <= rp:
            mid = (lp + rp) // 2
            guessed = guess(mid)
            if guessed == 0:
                return mid
            if guessed == -1:
                rp = mid-1
            elif guessed == 1:
                lp = mid+1