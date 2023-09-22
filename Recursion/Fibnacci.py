"""
Display the Nth Fib number using recursion

"""



def Fib(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return Fib(n-1) + Fib(n-2)


n = int(input("Enter the Number: "))

print(Fib(n))