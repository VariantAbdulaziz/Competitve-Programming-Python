# source: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# strategy: two pointers | sliding window
class Solution:
    def maxProfit(self, prices) -> int:
        res = 0
        l = 0
        for r in range(1, len(prices)):
            
            if prices[r] < prices[l]:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
                
                
        return res