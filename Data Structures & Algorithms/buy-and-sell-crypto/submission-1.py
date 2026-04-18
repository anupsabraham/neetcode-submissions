class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1
        max_p = 0

        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
            else:
                max_p = max(max_p, prices[right] - prices[left])
            right += 1
        
        return max_p