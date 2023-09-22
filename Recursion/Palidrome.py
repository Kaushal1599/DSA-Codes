"""
Check string is palidrome or not using recusrion
"""

def check_palidrome(s,n,i):
    if i >= n:
        return True
    if (s[i] != s[n-i-1]):
        return False
    return check_palidrome(s,n,i+1)


s = input("Enter the String : " )

print(check_palidrome(s,len(s),0))

