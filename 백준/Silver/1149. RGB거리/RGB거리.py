import sys
N=int(sys.stdin.readline())
cost=[]
for i in range(N):
    cost+=[list(map(int,sys.stdin.readline().split()))]
dp=[cost[0][0],cost[0][1],cost[0][2]]
for i in range(1,N):
    cost[i][0]+=min(dp[1],dp[2])
    cost[i][1]+=min(dp[0],dp[2])
    cost[i][2]+=min(dp[0],dp[1])
    dp[0],dp[1],dp[2]=cost[i][0], cost[i][1],cost[i][2]
print(min(dp))