import sys
from collections import deque
T=int(sys.stdin.readline())
for i in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    table=[[0]*M for _ in range(N)]
    for i in range(K):
        x,y=map(int,sys.stdin.readline().split())
        table[y][x]=1
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    def BFS(y,x):
        queue=deque([[y,x]])
        table[y][x]=0
        while queue:
            y,x=queue.popleft()
            table[y][x]=0
            for i in range(4):
                x2=x+dx[i]
                y2=y+dy[i]
                if x2<0 or x2>=M or y2<0 or y2>=N:
                    continue
                if table[y2][x2]==1:
                    table[y2][x2]=0
                    queue.append([y2,x2])
        return
    num=0
    for y in range(N):
        for x in range(M):
            if table[y][x]==1:
                n=BFS(y,x)
                num+=1

    print(num)