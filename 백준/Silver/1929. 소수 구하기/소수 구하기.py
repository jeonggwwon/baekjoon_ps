import sys
import math
M,N=map(int,sys.stdin.readline().split())

prime=[True for i in range(N+1)]

prime[1]=False
for i in range(2,int(math.sqrt(N))+1):
    if prime[i]==True:
        j=2
        while i*j <=N:
            prime[i*j]=False
            j+=1
for i in range(M,N+1):
    if prime[i]==True:
        print(i)