"""
Find the min in the roated sorted array

"""

import sys

def min_roated_binaryS(arr):
    low = 0
    high = len(arr) -1
    ans = sys.maxsize

    while(low<=high):
        mid = (low+high)//2
        if arr[low] <= arr[mid]:  # left part is sorted 
            ans = min(arr[low],ans)
            low = mid+1
        else:
            ans = min(arr[mid],ans)
            high = mid-1
    return ans


arr = [7,8,0,1,2,3,4,5,6]

print(min_roated_binaryS(arr))


