import sys
sys.setrecursionlimit(10**5)
N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
cnt=0

for m in range(M):
    p1, p2 =map(int,sys.stdin.readline().split())
    graph[p1].append(p2)
    graph[p2].append(p1)

def DFS(start):
    global cnt
    visited[start]=1
    cnt+=1
    for next in graph[start]:
        if visited[next]==0:
            DFS(next)
    return

DFS(1)
print(cnt-1)