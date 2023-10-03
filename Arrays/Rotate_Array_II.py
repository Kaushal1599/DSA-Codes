"""
Left Rotate array by D places 

"""

"""
Please not that if the d is given more than N always take the d as d % N 

Reason : - After N rotation the original array will come

"""
# Brute Force solution 

def Rotate(arr,n,d):
    temp = []
    for i in range(0,d):
        temp.append(arr[i])

    for i in range(d,n):
        arr[i-d] = arr[i]

    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]
    print(arr)


# Optimal solution 
"""
Special Solution 

Just observe things 

eg arr = [1,2,3,4,5,6,7]  d = 3 

    new arr = [3,2,1,7,6,5,4] -> reverse it - > [4,5,6,7,1,2,3] - > Ans

So, the ans is now 

Reverse(a,a+d)
Reverse(a+d,a+n)
Reverse(a,a+n)
"""


def Optimal_Rotate(arr,n,d):
    new_arr = arr[:d]
    new_arr1 = arr[d:n]
    new_arr.reverse()
    new_arr1.reverse()
    new_arr.extend(new_arr1)
    new_arr.reverse()
    print(new_arr)

arr = [1,2,3,4,5]

d = int(input("Enter the value of D: "))

#Rotate(arr,len(arr),d%len(arr))

Optimal_Rotate(arr,len(arr),d%len(arr))

    
