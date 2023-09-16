"""
Single element in the sorted array

arr = [1,1,2,2,3,3,4,5,5,6,6]

other number -> Twice

Only once 
"""

def Find_SingElement(arr):
    low = 1
    high = len(arr) - 2
    n = len(arr)
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1] :
            return arr[mid]
        elif (mid % 2 == 1 and arr[mid-1] == arr[mid]) or (mid%2 == 0 and arr[mid] == arr[mid+1]):
            low=mid+1
        else:
            high=mid-1

arr = [1,1,2,2,3,4,4,5,5,6,6]

print(Find_SingElement(arr))


