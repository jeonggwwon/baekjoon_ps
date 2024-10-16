import sys
N=int(sys.stdin.readline())
result=[0]*(N+1)
result[0]=1
result[1]=1
for i in range(2,N+1):
    result[i]=(result[i-2]+result[i-1])%15746
print(result[N])