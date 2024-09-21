import sys
N,C=map(int,sys.stdin.readline().split())
x=[]
for i in range(N):
    x+=[int(sys.stdin.readline())]
x.sort()

start, end= 1, x[-1]-x[0]

while start<=end:
    global res
    cnt, cur= 1, x[0]
    mid = (start + end) // 2
    for i in range(1,N):
        if x[i]>=cur+mid:
            cnt+=1
            cur=x[i]
    if cnt>=C:
        res=mid
        start=mid+1
    elif cnt<C:
        end=mid-1
print(res)