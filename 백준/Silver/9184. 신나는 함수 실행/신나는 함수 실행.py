import sys
def w(a,b,c):
    if a<=0 or b<=0 or c<=0: # a,b,c <=0이면 1을 리턴
        return 1
    if a>20 or b>20 or c>20: # a,b,c >20이면 w(20,20,20)을 리턴
        return w(20,20,20)
    if result[a][b][c]: # result 리스트에 (a,b,c)가 존재한다면 리턴
        return result[a][b][c] # 아래 if-else문에서 계산에 사용될 값을 리턴
    # result 리스트에 값이 존재하지 않으면 (0이라면) 계산하기
    # 조건에 따라 계산하면 나중에 사용하기 위해 result에 저장
    if a<b<c:
        result[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
    else:
        result[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return result[a][b][c] # 계산이 끝나면 정답을 리턴

# w함수 계산에 사용할 dp 리스트를 미리 초기화
result=[[[0]*21 for i in range(21)] for i in range(21)]

while True:
    a,b,c=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1 and c==-1: # 종료
        break

    print('w(', a, ', ', b, ', ', c, ') = ', w(a,b,c), sep='')