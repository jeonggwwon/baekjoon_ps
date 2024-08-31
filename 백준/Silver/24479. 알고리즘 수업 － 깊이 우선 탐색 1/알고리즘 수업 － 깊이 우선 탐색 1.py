import sys
sys.setrecursionlimit(10**5)
N,M,R=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
n=1
def DFS(g,r,v):
    global n
    v[r]=n
    for i in g[r]:
        if v[i]==0:
            n+=1
            DFS(g,i,v)
for m in range(M):
    p1, p2 =map(int,sys.stdin.readline().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
for i in range(N+1):
    graph[i].sort()
DFS(graph,R,visited)
for i in range(1,N+1):
    print(visited[i])