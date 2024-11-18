import sys
sys.setrecursionlimit(10**5)
N=int(sys.stdin.readline())
painting=[]
for i in range(N):
    painting+=[list(sys.stdin.readline().rstrip())]
cnt1, cnt2 = 0, 0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
visited=[[0]*N for _ in range(N)]

def DFS1(x, y, color):
    if x<0 or x>=N or y<0 or y>=N:
        return
    if painting[x][y]==color and visited[x][y]==0:
        visited[x][y]+=1
        for i in range(4):
            x2=x+dx[i]
            y2=y+dy[i]
            DFS1(x2,y2,color)

def DFS2(x, y, color):
    if x<0 or x>=N or y<0 or y>=N:
        return
    if visited[x][y]==1:
        if color=='B':
            if painting[x][y] == color:
                visited[x][y] += 1
                for i in range(4):
                    x2=x+dx[i]
                    y2=y+dy[i]
                    DFS2(x2,y2,color)
        else:
            if painting[x][y]=='R' or painting[x][y]=='G':
                visited[x][y] += 1
                for i in range(4):
                    x2=x+dx[i]
                    y2=y+dy[i]
                    DFS2(x2,y2,color)

for x in range(N):
    for y in range(N):
        if visited[x][y]==0:
            DFS1(x,y,painting[x][y])
            cnt1+=1

for x in range(N):
    for y in range(N):
        if visited[x][y]==1:
            DFS2(x,y,painting[x][y])
            cnt2+=1

print(cnt1, cnt2)