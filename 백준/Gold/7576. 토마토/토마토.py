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

# 처음에는 code 24~ 에서 이중 for문을 돌면서 익은 토마토마다 계산했다.
# 그러면 메모리 초과
# 큐에 시작점을 다 넣어두고 동시에 출발해야겠다 생각
# code 19~ 에서 if문에 tomato[x2][y2]>tomato[x][y] 조건을 넣었었는데
# 이것때문에 메모리 초과
# 이전에 시작점에 다 넣어두고 시작하지 않을 때는 tomato에 이전 값이 남아있었어서
# 이 조건이 들어갔었지만, 시작점을 큐에 모두 넣어두고 시작하면
# 아직 방문하지 않은 점은 0인 상태이다.