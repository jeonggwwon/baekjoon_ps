import sys
from collections import deque
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr += [list(map(int, sys.stdin.readline().rstrip()))]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
num=0
result=[]

def DFS(x,y):
    global num
    if x<0 or x>=N or y<0 or y>=N:
        return
    if arr[x][y]==1:
        arr[x][y]=0
        num+=1
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            DFS(x2,y2)

for x in range(N):
    for y in range(N):
        if arr[x][y]==1:
            DFS(x,y)
            result.append(num)
            num=0
print(len(result))
result.sort()
for i in range(len(result)):
    print(result[i])