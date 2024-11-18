import sys
sys.setrecursionlimit(10**6)
K=int(sys.stdin.readline())

def DFS(start, mark):
    visited[start]=mark
    for next in graph[start]:
        if visited[next]==0:
            if DFS(next,-mark):
                pass
            else:
                return 0
        elif visited[next]==visited[start]:
            return 0
    return 1

for k in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph=[[] for _ in range(V+1)]
    visited=[0]*(V+1)
    binary=1

    for e in range(E):
        p1, p2 = map(int, sys.stdin.readline().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    for v in range(1,V+1):
        if visited[v]==0:
            binary=DFS(v,1)
            if binary==0:
                break

    if binary:
        print('YES')
    else:
        print('NO')