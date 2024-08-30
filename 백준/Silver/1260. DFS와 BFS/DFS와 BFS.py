import sys
from collections import deque

def DFS(g,s,v):
    v[s]=True
    print(s, end=' ')
    for i in g[s]:
        if not v[i]:
            DFS(g,i,v)
def BFS(g,s,v):
    q=deque([s])
    v[s]=True

    while q:
        n=q.popleft()
        print(n,end=' ')
        for i in g[n]:
            if not v[i]:
                q.append(i)
                v[i]=True

N,M,V=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited_DFS=[False]*(N+1)
visited_BFS=[False]*(N+1)
for m in range(M):
    p1, p2 =map(int,sys.stdin.readline().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
for i in range(N+1):
    graph[i].sort()
DFS(graph,V,visited_DFS)
print()
BFS(graph,V,visited_BFS)