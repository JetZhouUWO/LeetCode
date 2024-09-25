class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = prices[0]
        for p in prices[1:]:
            if p < buy_price:
                buy_price = p
            profit = max(profit, p - buy_price)
        return profit