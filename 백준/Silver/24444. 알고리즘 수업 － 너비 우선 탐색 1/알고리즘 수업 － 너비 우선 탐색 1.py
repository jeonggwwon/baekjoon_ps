import sys
from collections import deque
sys.setrecursionlimit(10**5)
N,M,R=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
visited=[0]*(N+1)
n=1
def BFS(g,s,v):
    global n
    q=deque([s])
    v[s]=n
    while q:
        num=q.popleft()
        for i in g[num]:
            if not v[i]:
                n+=1
                q.append(i)
                v[i]=n

for m in range(M):
    p1, p2 =map(int,sys.stdin.readline().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
for i in range(N+1):
    graph[i].sort()
BFS(graph,R,visited)
for i in range(1,N+1):
    print(visited[i])