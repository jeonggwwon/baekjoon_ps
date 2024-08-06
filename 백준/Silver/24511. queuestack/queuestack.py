import sys
from collections import deque
N=int(sys.stdin.readline())
A=deque(list(map(int,sys.stdin.readline().split())))
B=deque(list(map(int,sys.stdin.readline().split())))
M=int(sys.stdin.readline())
C=deque(list(map(int,sys.stdin.readline().split())))
out=deque([])
result=[]
for i in range(N):
    if A[i]==0:
        out.append(B[i])
for i in range(M):
    out.appendleft(C[i])
    result+=[out.pop()]
print(*result)