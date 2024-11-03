import sys
from collections import deque
M,N=map(int,sys.stdin.readline().split())
tomato=[]
for i in range(N):
    tomato+=[list(map(int,sys.stdin.readline().split()))]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
queue=deque()

def BFS():
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            if x2<0 or x2>=N or y2<0 or y2>=M:
                continue
            if tomato[x2][y2]==0:
                tomato[x2][y2]=tomato[x][y]+1
                queue.append([x2,y2])


for _x in range(N):
    for _y in range(M):
        if tomato[_x][_y]==1:
            queue.append([_x,_y])
BFS()
res=0
for row in tomato:
    if 0 in row:
        print(-1)
        exit(0)
    res=max(res,max(row))
print(res-1)