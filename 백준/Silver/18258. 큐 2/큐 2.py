import sys
from collections import deque
N=int(sys.stdin.readline())
dq=deque([])
for i in range(N):
    ins=list(sys.stdin.readline().split())
    if ins[0]=='push':
        dq.append(ins[1])
    elif ins[0]=='pop':
        if len(dq)==0:
            print(-1)
        else:
            print(dq.popleft())
    elif ins[0]=='size':
        print(len(dq))
    elif ins[0]=='empty':
        if len(dq)==0:
            print(1)
        else:
            print(0)
    elif ins[0]=='front':
        if len(dq)==0:
            print(-1)
        else:
            print(dq[0])
    elif ins[0]=='back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])