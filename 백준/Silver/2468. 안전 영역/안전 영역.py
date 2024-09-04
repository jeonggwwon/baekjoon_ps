import copy
import sys
from collections import deque
sys.setrecursionlimit(100000)
N=int(sys.stdin.readline())
space=[]
for i in range(N):
    space += [list(map(int, sys.stdin.readline().split()))]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
num= 0
result, arr= [], []
table=copy.deepcopy(space)
def DFS(x,y,h):
    global num
    if x<0 or x>=N or y<0 or y>=N:
        return
    if space[x][y]>h:
        num+=1
        space[x][y]=0
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            DFS(x2,y2,h)

for i in range(max(map(max,space))):
    space = copy.deepcopy(table)
    num = 0
    for x in range(N):
        for y in range(N):
            if space[x][y]>i:
                DFS(x, y, i)
                arr.append(num)
    result.append(len(arr))
    arr=[]
print(max(result))