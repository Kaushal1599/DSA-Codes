"""
Remove Duplicates in place form sorted arrays

eg = [1,1,2,2,2,3,3]

ans = [1,2,3,_,_,_,_] we don't care what is in the remainnig place

Brute Force  approach 

Add the elements in the set data structures ( Time complexity will be (NlogN))

"""

#optimal solution is using two pointers approach


def Remove_Duplicates(arr):
    i = 0
    for j in arr:
        if j != arr[i]:
            i+=1
            arr[i] = j
    print(arr)
    return i+1 # this will be size of the array after removing duplicates 

arr = [1,1,2,2,2,3,3,4]

print(Remove_Duplicates(arr))

