import sys
import math
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    min,max=n, 2*n
    prime=[1 for i in range(max+1)]
    prime[1]=0
    for i in range(2,int(math.sqrt(max))+1):
        if prime[i]==1:
            j=2
            while i*j<=max:
                prime[i*j]=0
                j+=1
    num=0
    for i in range(min+1,max+1):
        if prime[i]==1:
            num+=1
    print(num)