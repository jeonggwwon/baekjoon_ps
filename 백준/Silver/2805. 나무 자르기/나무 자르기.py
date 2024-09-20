import sys
N, M= map(int,sys.stdin.readline().split())
tree=list(map(int, sys.stdin.readline().split()))

start, end= 0, max(tree)

while start<=end:
    sum = 0
    mid = (start + end) // 2
    for i in range(N):
        if tree[i]>mid:
            sum+=(tree[i]-mid)
    if sum>=M:
        start=mid+1
    elif sum<M:
        end=mid-1
print(end)