"""
Print Factorial of N using recursion

"""

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = int(input("Enter the value of N: "))
print(fact(n))
