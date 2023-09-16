"""
Returns the min integer K such that Koko can eat all bananas with h hours

eg
 
Piles = [3,6,7,11] , h = 8


"""
import math,sys

def koko_eating_bananas(piles,h):
    low = 1
    high = max(piles)
    ans = sys.maxsize

    while (low<=high):
        mid = (low+high)//2
        req_time = 0

        for i in piles:
            req_time += math.ceil(i/mid )
            
        if req_time <= h :
            ans = min(mid,ans)
            high = mid-1
        else:
            low = mid +1
    return ans


        
Piles = [3,6,7,11] 
h = 9

print(koko_eating_bananas(Piles,h))
