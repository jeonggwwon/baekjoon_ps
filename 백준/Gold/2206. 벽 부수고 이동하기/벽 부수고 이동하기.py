import sys
from collections import deque
N, M=map(int,sys.stdin.readline().split())
table=[]
for i in range(N):
    table+=[list(map(int,sys.stdin.readline().rstrip()))]

visit=[[[0]*2 for i in range(M)] for i in range(N)]
visit[0][0][0]=1

dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(_x,_y,_c):
    queue=deque([[_x,_y,_c]])
    while queue:
        x,y,check=queue.popleft()
        if x==N-1 and y==M-1:
            return visit[x][y][check]
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            if x2<0 or x2>=N or y2<0 or y2>=M:
                continue
            if table[x2][y2]==0 and visit[x2][y2][check]==0:
                visit[x2][y2][check] = visit[x][y][check] + 1
                queue.append([x2,y2,check])
            elif check==0 and table[x2][y2]==1:
                visit[x2][y2][1] = visit[x][y][0] + 1
                queue.append([x2,y2,1])
    return -1

print(bfs(0,0,0))
