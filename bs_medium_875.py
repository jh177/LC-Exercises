def minEatingSpeed(piles, h):
        if len(piles) == h: return max(piles)

        max_pile = max(piles)
        min_pile = min(piles)
        
        extra_hours = h - len(piles)
        
        min_k = max_pile // extra_hours        
        k = min_k
        
        while k < max_pile:
            if bs(piles, k):
                return True
            


def bs(piles, k):
    if max(piles <= 0): return True


