"""
Count the Subsequence with sum = k 

"""

def Count_SubSeq(arr,n,i,sum,k):
    if i == n :
        if sum == k:
            return 1
        else:
            return 0
        
    sum+=arr[i]

    left = Count_SubSeq(arr,n,i+1,sum,k)

    sum -= arr[i]

    right = Count_SubSeq(arr,n,i+1,sum,k)

    return left + right

arr = [1,2,1,2]

k = 3

print(Count_SubSeq(arr,len(arr),0,0,k))