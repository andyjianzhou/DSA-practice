class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.
        """
        smallestMap = {}
        if 0 in nums:
            return 0
        for i in range(len(nums)):
            offset = abs(nums[i])
            if offset not in smallestMap:
                smallestMap[offset] = nums[i]
            else:
                if nums[i] > smallestMap[offset]:
                    smallestMap[offset] = nums[i]
        return smallestMap[min(smallestMap.keys())]