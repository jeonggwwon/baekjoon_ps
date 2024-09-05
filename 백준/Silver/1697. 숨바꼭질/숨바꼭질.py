import sys
from collections import deque
N,K=map(int,sys.stdin.readline().split())
visited=[0]*(100001)
def BFS(n,k,v):
    q=deque([n])
    v[n]=1
    num=0
    if n==k:
        return num
    while q:
        for i in range(len(q)):
            p=q.popleft()
            for p2 in [p-1,p+1,p*2]:
                if 0<=p2<=100000 and v[p2]==0:
                    if p2==k:
                        num+=1
                        return num
                    q.append(p2)
                    v[p2]=1
        num+=1

print(BFS(N, K, visited))