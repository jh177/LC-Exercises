def maxProfit(prices):
    
    min_price = max(prices)
    max_profit = 0

    for p in prices:
        if p < min_price:
            min_price = p
        else:
            max_profit = max(max_profit, p-min_price)

    return max_profit