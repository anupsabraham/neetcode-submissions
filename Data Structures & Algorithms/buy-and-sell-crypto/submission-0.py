class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        
        lowest = prices[0]
        for p in prices:
            if p < lowest:
                lowest = p
            profit_max = max(profit_max, p-lowest)
        
        return profit_max