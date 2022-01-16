from re import L


def maxProfit(prices):
    max_profit = 0

    max_profit = 0

    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if max_profit < prices[j] - prices[i]:
                max_profit = prices[j] - prices[i]

    return max_profit
    
            


