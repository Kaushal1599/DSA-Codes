"""
Find Kth Missing Number

eg

arr = [2,3,4,7,11]  k =5 

[1,2,3,4,5,6,7,8,9,10,11]

1 is the I missing number

5 is the II missing numnber and soo on

Hence the 5th missing number is 9

"""

def MissingNumber(arr,k):
    low = 0
    high = len(arr) -1
    while(low<=high):
        mid = (low+high)//2
        missing = arr[mid] - (mid+1)
        if missing < k:
            low=mid+1
        else:
            high = mid-1

    return low+k

arr = [2,3,4,7,11]

k = 6

print(MissingNumber(arr,k))
