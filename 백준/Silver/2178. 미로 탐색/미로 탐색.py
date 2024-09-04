import sys
from collections import deque
N, M=map(int,sys.stdin.readline().split())
table=[]
for i in range(N):
    table+=[list(map(int,sys.stdin.readline().rstrip()))]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def BFS(x,y):
    queue=deque([[x,y]])
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            if x2<0 or x2>=N or y2<0 or y2>=M:
                continue
            if table[x2][y2]==1:
                table[x2][y2] = table[x][y]+1
                queue.append([x2, y2])
    return table[N-1][M-1]
print(BFS(0,0))