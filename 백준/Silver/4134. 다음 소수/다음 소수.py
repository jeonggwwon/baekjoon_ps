import sys
T=int(sys.stdin.readline())
def prime_check(x):
    for i in range(2,int(x**(1/2))+1):
        if x%i==0:
            return 0
    return 1
for i in range(T):
    n=int(sys.stdin.readline())
    while True:
        if n==0 or n==1 or n==2:
            print(2)
            break
        if prime_check(n):
            print(n)
            break
        else:
            n+=1