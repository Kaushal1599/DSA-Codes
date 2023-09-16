"""
Search insert position 

If present -> Return Index

if not -> Return the index as the array remain sorted 

Eg arr[1,2,4,7] k =6

return ind = 3 after inseration arr[1,2,4,6,7]

"""

# No need to worry just take the lowerbound of the given number

import sys

def lowerbound(arr,x):
    low = 0
    high = len(arr) - 1
    if arr[high] < x:
        return len(arr)
    ans = sys.maxsize
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] >= x :
            ans = mid # maybe my answer
            high = mid -1
        else:
            low = mid+1
    return ans


arr = [1,2,4,7]

x = int(input("Enter the value of x: "))

print(lowerbound(arr,x))




