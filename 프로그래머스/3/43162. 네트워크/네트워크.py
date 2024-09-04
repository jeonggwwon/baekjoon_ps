def DFS(t,s,v):
    v[s]=1
    for i in t[s]:
        if not v[i]:
            DFS(t,i,v)
def solution(n, computers):
    arr, table= [], [[]]
    visited=[0]*(n+1)
    for i in range(n):
        for j in range(n):
            if i==j:
                continue
            elif computers[i][j]==1:
                arr+=[j+1]
        table+=[arr]
        arr=[]
    for i in range(n+1):
        table[i].sort()
    answer=0
    for i in range(1,n+1):
        if visited[i]==0:
            DFS(table,i,visited)
            answer+=1
    return answer