"""
Search in Roated Sorted Array

arr[7,8,9,1,2,3,4,5,6] , target = 1

array is roated at 7

"""


# Try to identify the sorted half first so we can eliminate easily 

def Roated_BinaryS(arr,target):
    low = 0
    high = len(arr) -1
    
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == target :
            return "Found"
        
        if arr[low] <= arr[mid] : # it means the left part is sorted
            if arr[low] <= target <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:                    # it means the right part is sorted 
            if arr[mid] <= target <= arr[high]:
                low = mid+1
            else:
                high = mid -1 
    return "Not Found"

arr = [7,8,9,1,2,3,4,5,6]
target = int(input("Enter the Value of Target: "))

print(Roated_BinaryS(arr,target))

