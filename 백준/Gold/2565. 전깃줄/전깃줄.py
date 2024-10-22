import sys
N=int(sys.stdin.readline())
cable=[]
for i in range(N):
    cable+=[list(map(int,sys.stdin.readline().split()))]
cable.sort()
# A의 전깃줄 위치를 기준으로 오름차순 정렬한다.
# 그러면 B의 전깃줄은 A의 전깃줄 위치를 인덱스 삼아 인덱스 기준 오름차순 정렬하게 된다.
# 전깃줄이 교차하지 않으려면 B의 전깃줄도 오름차순으로 정렬되면 된다.
# 11053번에서처럼 가장 긴 증가하는 부분 수열을 구하면 된다.
dp=[1]*N # 자기 자신을 길이 1로 간주하므로 모두 1로 초기화
for i in range(1,N):
    tmp=[]
    # 부분 수열의 마지막 인덱스가 i일 때, 증가하는 부분 수열의 최대 길이 저장
    for j in range(0,i):
        if cable[j][1]<cable[i][1]:
            # 인덱스 i의 값보다 작다면 그 인덱스의 dp를 tmp에 추가
            tmp+=[dp[j]]
    if len(tmp)>0:
        # tmp에 추가된 값이 있다면,
        # = 인덱스 i 이전에, 인덱스 i의 값보다 작은 값이 있다면
        dp[i]+=max(tmp)
        # 그 중 그 값까지의 부분 수열의 길이가 가장 긴 값 + 인덱스 i 값 (길이 초기값1)
        # = 인덱스 i까지의 가장 긴 증가하는 부분 수열의 길이
print(N-max(dp))
# max(dp) = 교차하지 않게 걸 수 있는 전깃줄의 최댓값
# 따라서 N-max(dp)가 제거해야 하는 전깃줄의 최소 개수이다.