# Two solutions
#1. 
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums

#2.
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lp, rp = 0, 1
        while rp < len(nums) and lp < len(nums):
            nums[rp] += nums[lp]
            lp += 1
            rp += 1
        return nums

        