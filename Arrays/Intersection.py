"""
Intersection of two sorted array

A = [1,2,2,3,3,4,5,6]

B = [2,3,3,5,6,6,7]

intersection = [2,3,3,5,6]

Brute Force -> Maintain a visted array for any one array and then traverse the any array and check for every element in other array

if found just mark that element as visited that will help us to know that the elements is already used and we can't use this elements again

"""


#optimal solution using two pointers approach

def Intersection(arr1,arr2):
    i = 0
    j = 0
    intersect = []
    n = len(arr1)
    m = len(arr2)

    while(i<n and j<m):
        if arr1[i] < arr2[j]:
            i+=1
        elif arr2[j] < arr1[i]:
            j+=1
        else:
            intersect.append(arr1[i])
            i+=1
            j+=1

    return intersect



A = [1,2,2,3,3,4,5,6]

B = [2,3,3,5,6,6,7]

print(Intersection(A,B))



