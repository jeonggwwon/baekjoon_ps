# dp의 냅색 알고리즘 사용
import sys
N, K=map(int,sys.stdin.readline().split())
item=[[0,0]] # dp가 인덱스 (1,1)부터 시작하므로
for i in range(N):
    item+=[list(map(int,sys.stdin.readline().split()))]
dp=[[0]*(K+1) for i in range(N+1)]
# 2차원 배열, 행: 물건의 무게W, 열: 배낭에 담을 수 있는 최대 무게 0~K
for i in range(1,N+1): # 행
    for j in range(1,K+1): # 열
        if j>=item[i][0]:
            # 담을 물건의 무게W가 배낭에 담을 수 있는 최대 무게보다 작다면
            # 1. 같은 열에서 이전 행(W)의 최대가치
            # 2. 현재 행의 무게(W)를 더했을 때 배낭이 꽉 채워질 때의 최대 가치
            # 둘 중 더 가치가 큰 값을 저장
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-item[i][0]]+item[i][1])
        else: # 무게가 배낭보다 크다면 같은 열에서 이전 행에서의 최대 가치를 저장
            dp[i][j]=dp[i-1][j]
print(max(map(max,dp)))