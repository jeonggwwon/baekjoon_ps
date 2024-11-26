import sys
from collections import deque
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
dp=[1]*N
for i in range(N):
    for j in range(i):
        if A[j]<A[i]:
            dp[i]=max(dp[i],dp[j]+1)

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