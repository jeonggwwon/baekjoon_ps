import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
A_rev=A[::-1]

dp_left=[1]*N
dp_right=[1]*N
# 인덱스가 A에서의 인덱스에 해당
# 자기 자신을 길이 1로 간주하므로 모두 1로 초기화
for i in range(1,N):
    temp_left = []
    # 부분 수열의 마지막 인덱스가 i일 때, 증가하는 부분 수열의 최대 길이 저장
    for j in range(0,i):
        if A[j]<A[i]:
            # 인덱스 i의 값보다 작다면 그 인덱스의 dp_left를 temp_left에 추가
            temp_left+=[dp_left[j]]
    if len(temp_left)>0:
        # temp_left에 추가된 값이 있다면,
        # = 인덱스 i 이전에, 인덱스 i의 값보다 작은 값이 있다면
        dp_left[i]+=max(temp_left)
        # 그 중 그 값까지의 부분 수열의 길이가 가장 긴 값 + 인덱스 i 값 (길이 초기값1)
        # = 인덱스 i까지의 가장 긴 증가하는 부분 수열의 길이

for i in range(1,N):
    temp_right=[]
    for j in range(0,i):
        if A_rev[j]<A_rev[i]:
            temp_right+=[dp_right[j]]
    if len(temp_right)>0:
        dp_right[i]+=max(temp_right)

dp=[]
for i in range(N):
    dp+=[dp_left[i]+dp_right[N-1-i]]
print(max(dp)-1)