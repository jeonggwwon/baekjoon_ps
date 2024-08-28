import sys
from collections import deque
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
result=deque([0]*n)
result[0]=arr[0]
for i in range(1,n):
    result[i]=max(result[i-1]+arr[i],arr[i])
print(max(result))