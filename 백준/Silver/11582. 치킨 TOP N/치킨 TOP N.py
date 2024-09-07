import sys
N=int(sys.stdin.readline())
data=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())

idx=N//k
result=list()

for i in range(0,N,idx):
    result=data[i:i+idx]
    result.sort()
    data[i:i+idx]=result[:]

print(*data)