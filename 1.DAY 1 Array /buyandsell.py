#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=prices[0]
        profit=0
        p=0
        for i in range(0,len(prices)):
            m=min(m,prices[i])
            p=prices[i]-m
            profit=max(profit,p)
        return profit
