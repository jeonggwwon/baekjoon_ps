import sys
K, N=map(int,sys.stdin.readline().split())
line=[]
for i in range(K):
    line+=[int(sys.stdin.readline())]

start, end= 1, max(line)

while start<=end:
    cnt = 0
    mid = (start + end) // 2
    for i in range(K):
        cnt+=line[i]//mid
    if cnt>=N:
        start=mid+1
    elif cnt<N:
        end=mid-1
print(end)