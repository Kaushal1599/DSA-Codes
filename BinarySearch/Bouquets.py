"""
Find the min no of days to make M bouquets 

eg 

Bloomday = [7,7,7,7,13,11,12,7]

m = 2 , k =3 

M -> no of bouquets we need to make

K -> adjacent flowers required to make a bouquet

"""

import sys

def IsPossible(arr,m,k,days):
    count = 0
    no_of_bouquets = 0
    for i in arr:
        if days >= i:
            count+=1
        else:
            no_of_bouquets += count/k
            count = 0
    no_of_bouquets+= count/k
    if no_of_bouquets >= m:
        return True
    else:
        return False


def bouquets(arr,m,k):
    low = min(arr)
    high = max(arr)
    ans = sys.maxsize
    while(low<=high):
        

        mid = (low+high)//2

        if IsPossible(arr,m,k,mid) == True:
            ans = min(mid,ans)
            high = mid -1
        else:
            low = mid +1
    return ans



Bloomday = [7,7,7,7,13,11,12,7]
m = 2 
k =3 
#print(IsPossible(Bloomday,m,k,11))

print(bouquets(Bloomday,m,k))
