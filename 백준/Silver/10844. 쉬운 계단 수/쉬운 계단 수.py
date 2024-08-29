import sys
N=int(sys.stdin.readline())
stair=[0]+[1]*9
result=[[],stair]
for j in range(2,N+1):
    stair =[0]+[1]*9
    stair[0]=result[j-1][1]
    for i in range(1,9):
        stair[i]=result[j-1][i-1]+result[j-1][i+1]
    stair[9]=result[j-1][8]
    result+=[stair]
print(sum(result[N])%10**9)