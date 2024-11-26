import sys
from collections import deque
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[1]*N
for i in range(1,N):
    temp=[]
    for j in range(0,i):
        if A[j]<A[i]:
            temp+=[dp[j]]
    if len(temp)>0:
        dp[i]+=max(temp)

result=[0]*max(dp)
for i in range(max(dp),0,-1):
    if i==max(dp):
        result[i-1]=A[dp.index(i)]
        continue
    for j in range(N):
        if dp[j]==i and A[j]<result[i]:
            result[i-1]=A[j]
            break

print(max(dp))
print(*result)