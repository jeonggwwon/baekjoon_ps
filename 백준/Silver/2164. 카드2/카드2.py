import sys
from collections import deque
N=int(sys.stdin.readline())
dq=deque([])
for i in range(1,N+1):
    dq.append(i)
check=0
while True:
    if len(dq)==1:
        print(dq[0])
        break
    if check==1:
        dq.append(dq[0])
        dq.popleft()
        check=0
    elif check==0:
        dq.popleft()
        check=1