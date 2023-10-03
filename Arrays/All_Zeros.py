"""
Move all zeros to the end of the array 

Brute Force approach simple take a temp array load all the non zero values in it 

Now traverse the original array and put all the non zero array from temp to the original array and at last just add 0

"""

#Optimal Approach using two pointers approach


def All_Zeros(arr,n):
    index = -1
    for i in range(0,n):
        if arr[i] == 0:
            index = i
            break

    for j in range(index+1,n):
        if arr[j] != 0:
            arr[j],arr[index] = arr[index], arr[j]
            index+=1
    print(arr)
    
arr = [1,0,2,3,2,0,0,4,5,1]

All_Zeros(arr,len(arr))
        