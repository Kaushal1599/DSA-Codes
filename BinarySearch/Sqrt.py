"""
Find the Sqrt of any integer using binary search

n = 25 -> 5

n = 30 -> 5

n = 35 -> 5

n = 40 -> 6

"""

def sqrt(n):
    low = 1
    high = n//2
    ans = 0

    while(low<=high):
        mid = (low+high)//2
        if mid * mid > n:
            high = mid -1
        else:
            ans = mid
            low = mid +1
    return ans


n = int(input("Enter the Number: "))
print(sqrt(n))
