class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof, i, j = 0, 0, 1
        while j<len(prices):
            if prices[i] < prices[j]:
                values = prices[j] - prices[i]
                prof = max(prof,values)
            else:
                i = j
            j+=1
        return prof