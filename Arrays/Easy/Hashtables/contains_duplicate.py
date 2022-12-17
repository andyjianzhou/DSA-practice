#1. Using a hash table

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}
        for i, v in enumerate(nums):
            if v in prevMap:
                return True
            prevMap[v] = i
        return False