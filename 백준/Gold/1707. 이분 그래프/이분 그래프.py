import sys
sys.setrecursionlimit(21000)
K=int(sys.stdin.readline())

def DFS(start):
    global binary
    for next in graph[start]:
        if visited[next]==0:
            if visited[start]==1:
                visited[next]=-1
            else:
                visited[next]=1
            DFS(next)
        elif visited[next]==visited[start]:
            binary=0
            return


for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    binary=1
    for e in range(E):
        p1, p2 = map(int, sys.stdin.readline().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    for v in range(1,V+1):
        if visited[v]==0:
            visited[v]=1
            DFS(v)
            if binary==0:
                break
    if binary:
        print('YES')
    else:
        print('NO')