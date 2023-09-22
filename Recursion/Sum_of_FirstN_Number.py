"""
Sum of first N Numbers

"""

#First way of paramtised way
def Sum_Paramtised_way(i,sum):
    if i < 1:
        print(sum)
        return
    Sum_Paramtised_way(i-1,sum+i)

#Functional way (without parameter)

def Sum_without_parameter(n):
    if n == 0:
        return 0
    return n + Sum_without_parameter(n-1)
    



n = int(input("Enter the Value of N: "))
Sum_Paramtised_way(n,0)
print(Sum_without_parameter(n))