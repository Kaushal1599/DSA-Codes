"""
Find the first and Last occurrence 

arr = [2,4,6,8,8,8,11,13]

x = 8 , output = 3,5

"""
# Pretty Easy for the first occurrence just find the lowerBound and for second occurrence find the upperbound - 1 

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

arr = [2,4,6,8,8,8,11,13]
x = int(input("Enter the Value of X: "))

firstOc = lowerbound(arr,x)
SecondOc = Upperbound(arr,x) -1

print(firstOc,SecondOc)