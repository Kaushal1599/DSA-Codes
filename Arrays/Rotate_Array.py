"""
Left Rotate Array by one place

arr = [1,2,3,4,5] - >  [2,3,4,5,1]

"""

# no brute better optimal only one solution 

def Rotate(arr,n):
    temp = arr[0]
    for i in range(1,n):
        arr[i-1] = arr[i]

    arr[n-1] = temp

    print(arr)

arr = [1,2,3,4,5]

Rotate(arr,len(arr))
