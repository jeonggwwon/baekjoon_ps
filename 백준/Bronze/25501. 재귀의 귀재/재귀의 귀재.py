import sys

def recursion(str,l,r,num):
    if l>= r:
        return [1, num]
    elif str[l]!=str[r]:
        return [0, num]
    else:
        num+=1
        return recursion(str,l+1,r-1,num)

def isPalindrome(str,num):
    num+=1
    return recursion(str,0,len(str)-1,num)

T=int(sys.stdin.readline())
num=0
for i in range(T):
    S=sys.stdin.readline().rstrip()
    print(*isPalindrome(S,num))