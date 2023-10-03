"""
Find the Second Largerst element in an array 

Brute Force approach 

- > Sort the array and print in the a[n-2] element ( time complexity is O(NlogN))

"""


#better solution (Time Complexity is O(2N))

def SecondLargest(arr):
    largest = max(arr)
    slargest = -1
    for i in arr:
        if i > slargest and i != largest:
            slargest = i

    return slargest


#Optimal Solution (Time complexity is O(N))


def Optimal_SecondLargest(arr):
    largest = arr[0]
    slargest = -1

    for i in arr:
        if i > largest:
            slargest = largest
            largest = i
        elif i < largest and i > slargest:
            slargest = i
    return slargest

arr = [1,2,3,4,5,6,7]

print(SecondLargest(arr))
print(Optimal_SecondLargest(arr))