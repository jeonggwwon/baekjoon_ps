import sys
N, K=map(int,sys.stdin.readline().split())
A=list(map(int,sys.stdin.readline().split()))
tmp=[0]*N
cnt, res= 0, 0

def merge(A,p,q,r):
    global cnt, res
    i,j,t=p,q+1,0
    while i<=q and j<=r:
        if A[i]<=A[j]:
            tmp[t]=A[i]
            t+=1
            i+=1
        else:
            tmp[t]=A[j]
            t+=1
            j+=1
    while i<=q:
        tmp[t] = A[i]
        t += 1
        i += 1
    while j<=r:
        tmp[t] = A[j]
        t += 1
        j += 1
    i,t=p,0
    while i<=r:
        cnt+=1
        A[i]=tmp[t]
        if cnt==K:
            print(A[i])
        i+=1
        t+=1

def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

merge_sort(A,0,N-1)
if cnt<K:
    print(-1)