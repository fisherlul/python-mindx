class Solution:
    import random as r
    def maxProfit(prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(len(prices)):
            stock = prices[i] - min_price
            max_profit = max(stock, max_profit)
            min_price = min(prices[i], min_price)
        print(max_profit)
            
    maxProfit([r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10), r.randint(1, 10)]) 