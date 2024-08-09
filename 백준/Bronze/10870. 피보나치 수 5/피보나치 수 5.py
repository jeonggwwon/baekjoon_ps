import sys
def F(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    elif n>=2:
        return F(n-1)+F(n-2)

n=int(sys.stdin.readline())
print(F(n))