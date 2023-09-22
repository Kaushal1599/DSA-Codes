"""
printing all the patterns related to numbers using Recursion

"""
#printing N -> 1
def printNumberOpposite(i,n):
    if i > n:
        return
    print(n)
    printNumberOpposite(i,n-1)
#print 1 -> N 
def printNumber(i,n):
    if i > n:
        return
    print(i)
    printNumber(i+1,n)


#printing 1 -> N without using +1
def printNumberWithoutplusOne(n):
    if n < 1:
        return
    printNumberWithoutplusOne(n-1)
    print(n)



n = int(input("Enter the value of N: "))
printNumber(1,n)
printNumberOpposite(1,n)
printNumberWithoutplusOne(n)
