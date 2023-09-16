"""

Find out how many times has an array been roated

arr = [3,4,5,1,2]  ans = 3

"""


# Observer clearly we just need to find out the index of the min in array :) 


import sys

def min_roated_binaryS(arr):
    low = 0
    high = len(arr) -1
    ans = sys.maxsize
    ind =-1
    while(low<=high):
        mid = (low+high)//2
        if arr[low] <= arr[mid]:  # left part is sorted 
            if arr[low] < ans:
                ans = arr[low]
                ind = low
            low = mid+1
        else:                    # right part is sorted 
            if arr[mid] < ans:
                ans = arr[mid]
                ind = mid
            high = mid-1
    return ind


arr = [7,8,9,10,1,3,4,5,6]

print(min_roated_binaryS(arr))