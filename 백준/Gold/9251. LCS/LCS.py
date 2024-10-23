import sys
s1=list(sys.stdin.readline().rstrip())
s2=list(sys.stdin.readline().rstrip())
dp=[[0]*(len(s2)+1) for i in range(len(s1)+1)]
# s1, s2를 행과 열로 0으로 초기화 된 2차원 배열 생성
# 해당하는 행과 열까지의 길이 s1과 s2 사이에 공통 부분 수열의 최대 길이 저장
# 행과 열이 1일 때 이전값 0을 가져와야 하므로, 2차원 배열은 (len(s1)+1)*(len(s2)+1)이다.
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        # dp[1][1]부터 시작한다.
        if s1[i-1]==s2[j-1]: # 현재 행과 열의 문자가 같다면
            dp[i][j]=dp[i-1][j-1]+1
            # 예시 입력의 행렬을 그려보면 규칙성을 찾을 수 있다.
            # 행과 열의 문자가 같을 때는 각 행과 열 -1의 값에 +1 한 것
        else: # 현재 행과 열의 문자가 같지 않다면
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            # 이전 열이나 이전 행의 값 중 큰 값을 따른다.
print(max(map(max,dp)))
# 행렬 전체에서 가장 큰 값이 가장 긴 LCS이다.