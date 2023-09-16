"""
Find the least capacity to ship packages within D Days

eg 

weight = [1,2,3,4,5,6,7,8,9,10] , Days = 5

output = 15

day 1 -> [1,2,3,4,5]
day 2 -> [5,6]
day 3 -> [7,8]
day 4 -> [9]
day 5 -> [10]

"""
import sys
def daysRequired(arr,capacity):
    load = 0
    days = 1
    for i in arr:
        if load + i > capacity:
            days+=1
            load = i
        else:
            load+=i
    return days

def leastWeight(arr,days):
    low = max(arr)
    high = sum(arr)
    ans = sys.maxsize
    while(low<=high):
        mid = (low+high)//2
        if daysRequired(arr,mid) <= days:
            ans = min(ans,mid)
            high = mid -1
        else:
            low = mid+1
    return ans


weight = [1,2,3,4,5,6,7,8,9,10] 
Days = 5
#print(daysRequired(weight,11))

print(leastWeight(weight,Days))
