import sys
from collections import deque
N, K=map(int,sys.stdin.readline().split())
dq=deque([])
for i in range(1,N+1):
    dq.append(i)
result=[]
while True:
    dq.rotate(-(K-1))
    result+=[dq[0]]
    dq.popleft()
    if len(dq) == 0:
        print('<', end='')
        for i in range(N):
            if i == N - 1:
                print(result[i], end='>')
            else:
                print(result[i], end=', ')
        break