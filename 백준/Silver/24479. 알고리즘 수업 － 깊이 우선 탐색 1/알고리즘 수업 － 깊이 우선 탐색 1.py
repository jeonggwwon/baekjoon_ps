import sys
from collections import defaultdict
from collections import  deque

N, M, R = map(int, sys.stdin.readline().split())
answer = [0]*N
visited = [False]*N
visited_node = deque([R])
graph = defaultdict(list)
cnt = 1

def DFS(V, graph, R):
    global cnt
    if visited[V-1] == False:
        visited[V-1] = True
        answer[V-1] = cnt
        cnt += 1

        visited_node.extendleft(sorted(graph[V], reverse= True))
        if visited_node:
            V = visited_node.popleft()
        else:
            pass
        DFS(V,graph, R)
        
for _ in range(M):
    E1, E2 = map(int, sys.stdin.readline().split())
    graph[E1].append(E2)
    graph[E2].append(E1)

while visited_node:
    V = visited_node.popleft()
    DFS(V, graph, visited)

answer = list(map(str, answer))
print('\n'.join(answer))