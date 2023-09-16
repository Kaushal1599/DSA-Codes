"""
Peak element is if 

arr[i-1] < arr[i] > arr[i+1]
eg

arr = [1,2,3,4,5,6,7,8,5,1]  ans 8

arr = [1,2,1,3,5,6,4] ans 2 or 6

arr [ 1,2,3,4,5] ans 5

arr = [5,4,3,2,1] ans = 5

"""

def PeakElement(arr):
    n = len(arr)
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    low = 1
    high = n-2
    while(low<=high):
        mid = (low+high)//2
        if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid-1]:
            return arr[mid]
        if arr[mid] > arr[mid -1]:
            low= mid+1
        else:
            high = mid -1
    return -1

arr=[1,2,3,4,5,6,7,8,5,1]

arr1 = [5,4,3,2,1]
arr2 = [1,2,3,4,5]

print(PeakElement(arr2))
        

