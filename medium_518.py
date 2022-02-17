class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self._change(amount, coins, 0, {})
        
        
    def _change(self, amount, coins, i, memo):
        if (amount, i) in memo: return memo[(amount,i)]
        
        if amount == 0: return 1
        
        if i == len(coins): return 0
        
        coin = coins[i]
        total = 0
        
        for qty in range(0, amount//coin+1):
            total += self._change(amount-qty*coin, coins, i+1, memo)
            
        memo[(amount, i)] = total
        return total