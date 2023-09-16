"""
Find the smallest divisor such that sum of all the divident of the array elements is less than or equal to the threshold given

eg

arr = [1,2,5,9] , threshold = 6

lets suppose divisor is 4

1/4 -> 1
2/4 -> 1
5/4 -> 2
9/4 -> 3 

1 + 1 + 2 + 3 = 7 now 7 is not less than or equal to 6 Hence 4 can't be the ans

"""
import math,sys

def DividentSumCheck(arr,divisor,threshold):
    divident_sum = 0
    for i in arr:
        divident_sum += math.ceil(i/divisor)
    if threshold >= divident_sum:
        return True
    else:
        return False

def SmallestDivisor(arr,threshold):
    low = 1
    high = max(arr)
    ans = sys.maxsize
    while(low<=high):
        mid = (low+high)//2
        if DividentSumCheck(arr,mid,threshold) == True:
            ans = min(mid,ans)
            high = mid -1
        else:
            low = mid+1

    return ans


arr = [1,2,5,9] 
threshold = 6

print(SmallestDivisor(arr,threshold))
