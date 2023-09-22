"""
Given a array and a target , Find all the unique combination in array 
where sum is equal to target.

NOTE : Combination should be sorted 

NOTE: Each number may only be used once in the combination

NOTE: Solution not contains duplicates

"""

def combination2(arr,ind,n,t,ds):
    
    if t == 0:
        print(ds)
        return 
    i = ind
    while(i<n):
        if i > ind and arr[i] == arr[i-1]:
            i+=1
            continue
        if arr[i] > t:
            break
        ds.append(arr[i])

        combination2(arr,i+1,n,t-arr[i],ds)

        ds.remove(arr[i])

        i+=1

arr = [10,1,2,7,6,1,5] 
arr.sort()
t = 8

combination2(arr,0,len(arr),t,[])

