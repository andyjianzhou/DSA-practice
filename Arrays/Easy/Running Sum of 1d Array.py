# Two solutions
#1. Simple for loop
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        return nums

#2. Two pointer
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        lp, rp = 0, 1
        while rp < len(nums) and lp < len(nums):
            nums[rp] += nums[lp]
            lp += 1
            rp += 1
        return nums

# How this works is that we have two pointers, one at the beginning and one at the end. 
# We add the value at the end pointer to the value at the beginning pointer and then move both pointers up by one. 
# We do this until the end pointer reaches the end of the array. This is a prefix sum problem.