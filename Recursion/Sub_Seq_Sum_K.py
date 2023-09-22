"""
Part I 
print all the subseq whose sum is K 

eg

arr = [1,2,1] -> sum = 2

1,1
2


Part II 

Print any subseq whose sum is K

"""


def Sum_K_all(arr,n,i,k,ds,sum):
    if i == n:
        if sum == k:
            print(ds)
        return
    
    ds.append(arr[i])
    sum+=arr[i]
    #print(sum)
    Sum_K_all(arr,n,i+1,k,ds,sum)
    ds.remove(arr[i])
    sum-=arr[i]
    Sum_K_all(arr,n,i+1,k,ds,sum)


def Sum_K_one(arr,n,i,k,ds,sum):
    if i == n:
        if sum == k:
            print(ds)
            return True
        return False

    ds.append(arr[i])
    sum+=arr[i]
    if Sum_K_one(arr,n,i+1,k,ds,sum) == True:
        return True
    sum -=arr[i]
    ds.remove(arr[i])
    if Sum_K_one(arr,n,i+1,k,ds,sum) == True:
        return True
    return False



arr = [1,2,1]

k = 2

Sum_K_all(arr,len(arr),0,k,[],0)
print("-------------------------------")
Sum_K_one(arr,len(arr),0,2,[],0)


