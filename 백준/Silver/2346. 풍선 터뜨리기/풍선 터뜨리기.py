import sys
from collections import deque
N=int(sys.stdin.readline())
balloon=deque([])
idx=deque([])
for i in range(N):
    idx.append(i+1)
order=[]
L=list(map(int,sys.stdin.readline().split()))
balloon.extend(L)
num=0
while True:
    order+=[idx[0]]
    num=balloon.popleft()
    idx.popleft()
    if len(idx) == 0:
        for i in range(N):
            print(order[i],end=' ')
        break
    if num<0:
        balloon.rotate(-num)
        idx.rotate(-num)
    else:
        balloon.rotate(-num+1)
        idx.rotate(-num+1)