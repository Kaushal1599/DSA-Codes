def BinaryS(arr,target):
    low=0
    high=len(arr)-1
    #print(len(arr))

    while(low<=high):
        mid = (low+high)//2
        if arr[mid] == target:
            return "Found"
        elif arr[mid] > target:
            high = mid -1
        else:
            low=mid+1
    
    return "Not Found"


arr = [10,12,14,15,17,19,20,22,25]

target = int(input("Enter The Number to find: "))
print(BinaryS(arr,target))


