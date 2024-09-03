import sys
from collections import deque
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr += [list(map(int, sys.stdin.readline().rstrip()))]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
result=[]

def BFS(x,y):
    queue=deque([[x,y]])
    arr[x][y]=0
    num=1
    while queue:
        x,y=queue.popleft()
        arr[x][y]=0
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            if x2<0 or x2>=N or y2<0 or y2>=N:
                continue
            if arr[x2][y2]==1:
                arr[x2][y2]=0
                queue.append([x2,y2])
                num+=1
    return num

for x in range(N):
    for y in range(N):
        if arr[x][y]==1:
            n=BFS(x,y)
            result.append(n)

print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])