from math import *


def minEatingSpeed(piles, h):
    l = 0
    r = max(piles)

    while l + 1 < r:
        mid = (l + r) // 2
        if (sum(ceil(i/mid) for i in piles)) > h:
            l = mid
        else:
            r = mid

    return r  
    
    
piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
