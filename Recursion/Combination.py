"""
Print all the unquie combination of array where the chosen number sum to target 

Note: You can pick any number any times

Eg: 

arr = [2,3,6,7] - > T = 7



"""

def combination(arr,ind,n,t,ds):
    if ind == n:
        if t == 0:
            print(ds)
        return 
    if arr[ind] <= t :
        ds.append(arr[ind])
        combination(arr,ind,n,t-arr[ind],ds)
        ds.remove(arr[ind])
    combination(arr,ind+1,n,t,ds)


arr = [2,3,6,7]

t = 7


combination(arr,0,len(arr),t,[])

    