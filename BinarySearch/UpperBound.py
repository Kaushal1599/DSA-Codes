"""
Upper bound :- Smallest index such that arr[ind] > x

eg :- arr[2,3,6,7,8,8,11,11,11,12]  

x = 6 -> Upperbound = 3 ,  x=11 -> Upperbound = 9 
"""
import sys

def Upperbound(arr,x):
    low = 0
    high = len(arr) - 1
    ans = sys.maxsize
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] > x :
            ans = mid # maybe my answer
            high = mid -1
        else:
            low = mid+1
    return ans


arr = [2,3,6,7,8,8,11,11,11,12]  

x = int(input("Enter the value of x: "))

print(Upperbound(arr,x))