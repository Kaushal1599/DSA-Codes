"""
Floor and Ceil in sorted array

Floor - > largest no in array <=x

Ceil - > smallest no in array >=x

eg 
arr[10,20,30,40,50] x =25

Floor =20 , Ceil = 30
"""
import sys

# if we observer clearly just we need to take the lowerbound of the given number that will be the Ceil 
def Ceil(arr,x):
    low = 0
    high = len(arr) - 1
    Ceil = sys.maxsize
    while(low<=high):
        mid = (low+high)//2

        if arr[mid] >= x :
            Ceil = arr[mid] # maybe my answer
            high = mid -1
        else:
            low = mid+1
    return Ceil

def floor(arr,x):
    low = 0
    high = len(arr) - 1
    floor = len(arr) - 1

    while(low<=high):
        mid = (low+high)//2

        if arr[mid] <=x:
            floor = arr[mid]

            low = mid +1
        else:
            high = mid-1
    return floor


arr = [10,20,30,40,45,50]
x = int(input("Enter the value of X: "))
print("Floor Value is: " ,floor(arr,x))
print("Ceil Value is: ", Ceil(arr,x))