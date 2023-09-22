"""
Print your name N times using Recursion

"""

def printName(i,n):
    if i > n:
        return
    print("Kaushal")
    printName(i+1,n)


n = int(input("Enter the value of N: "))
printName(1,n)
