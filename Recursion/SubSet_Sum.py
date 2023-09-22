"""
Given a array Print sum of all subsets in it, output should be printed in increasing order of sums

eg = arr[2,3]

output = 0,2,3,5

"""


def Subset_Sum(arr,ind,n,sum):
    if ind == n:
        print(sum)
        return
    Subset_Sum(arr,ind+1,n,sum)
    Subset_Sum(arr,ind+1,n,sum+arr[ind])


arr = [3,2]
Subset_Sum(arr,0,len(arr),0)
