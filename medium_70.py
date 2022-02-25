class Solution:
    def climbStairs(self, n: int) -> int:
        
        return self._climbStairs(n, {})
       
        
    def _climbStairs(self, n: int, memo):
        
        if n in memo: return memo[n]
        
        if n < 1: return 0
        if n == 1: 
            memo[n] = 1
            return memo[n]
        if n == 2: 
            memo[n] = 2
            return memo[n]
        
        memo[n] = self._climbStairs(n-1, memo) + self._climbStairs(n-2, memo)
        return memo[n]