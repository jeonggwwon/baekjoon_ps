import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    arr+=[list(sys.stdin.readline().split())]
    arr[i]+=[i]
arr.sort(key=lambda x: (int(x[0]), x[2]))
for i in range(N):
    print(*arr[i][0],sep='',end=' ')
    print(*arr[i][1],sep='')