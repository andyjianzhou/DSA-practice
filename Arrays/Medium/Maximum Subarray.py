#1. Two pointer approach
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Given an integer array nums, find the 
    subarray
    which has the largest sum and return its sum.
        """
        # two pointer method
        highest = nums[0]
        curSum = 0
        lp, rp = 0, 1
        while lp<= len(nums) and rp <= len(nums):
            curSum = sum(nums[lp:rp])
            if curSum < 0:
                curSum = 0
                lp = rp
            highest = max(highest,curSum)  
            rp += 1      
        return highest
 # works for all except all neg values
 # maybe just one for loop would do
        
