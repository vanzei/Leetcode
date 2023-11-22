class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            cProfit = prices[r] - prices[l]
            if maxP < cProfit:
                maxP = cProfit
            elif prices[l] > prices[r]:
                l = r
            r += 1
        return maxP
