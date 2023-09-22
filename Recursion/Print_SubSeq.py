"""
Print all the subseq of the given array 

"""


def Print_SubArray(ind,ds,arr,n):
    if ind >= n:
        print(ds)
        return 
    # condition for take the element 
    ds.append(arr[ind])
    Print_SubArray(ind+1,ds,arr,n)
    # condition for not take the element 
    ds.remove(arr[ind])
    Print_SubArray(ind+1,ds,arr,n)


arr = [3,1,2]
ds = []
n = len(arr) 

Print_SubArray(0,ds,arr,n)
