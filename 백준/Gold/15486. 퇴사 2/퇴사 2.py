import sys
N=int(sys.stdin.readline())
consult=[[0,0]]
dp=[0]*(N+2)
for i in range(N):
    consult+=[list(map(int,sys.stdin.readline().split()))]
for i in range(N,0,-1):
    if i+consult[i][0]-1<=N:
        if consult[i][1] + dp[i+consult[i][0]]>=dp[i+1]:
            dp[i] = consult[i][1] + dp[i+consult[i][0]]
        else:
            dp[i]=dp[i+1]
    else:
        dp[i]=dp[i+1]

print(dp[1])