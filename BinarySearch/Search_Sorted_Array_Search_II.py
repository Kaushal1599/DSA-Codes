"""
Search in Roated Sorted Array II (Data must contains duplicates also)

arr[3,1,2,3,3,3,3] , target = 1


"""


# Try to identify the sorted half first so we can eliminate easily 

def Roated_BinaryS(arr,target):
    low = 0
    high = len(arr) -1
    
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] == target :
            return "Found"
        if (arr[low] == arr[mid] == arr[high]):  # adding this condition will take care of duplicates 
            low = low+1
            high = high-1
            continue
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

arr = [3,1,2,3,3,3,3]
target = int(input("Enter the Value of Target: "))

print(Roated_BinaryS(arr,target))

