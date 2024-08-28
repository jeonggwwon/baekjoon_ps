import sys
from collections import deque
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
result=[1]*N
for i in range(1,N):
    temp = []
    for j in range(0,i):
        if A[j]<A[i]:
            temp+=[result[j]]
    if len(temp)>0:
        result[i]+=max(temp)
print(max(result))