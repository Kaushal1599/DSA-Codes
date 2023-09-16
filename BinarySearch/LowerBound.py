"""
Lower bound :- Smallest index such that arr[ind] >= x

eg :- arr[3,5,8,15,19] 

x = 8 -> lowerbound = 2 ,  x=9 -> lowerbound = 3 
"""
import sys

def lowerbound(arr,x):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] >= x :
            ans = mid # maybe my answer
            high = mid -1
        else:
            low = mid+1
    return ans


arr = [3,5,8,8,15,19]

x = int(input("Enter the value of x: "))

print(lowerbound(arr,x))
