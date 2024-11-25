import sys
T=int(sys.stdin.readline())

def fibonacci(n,fibo):
    if n==0 or n==1:
        return
    else:
        for i in range(2,n+1):
            fibo[i][0], fibo[i][1]= fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]
        return

for i in range(T):
    N=int(sys.stdin.readline())
    fibo=[[0,0] for _ in range(N+1)]
    fibo[0][0]=1
    if N>0:
        fibo[1][1]=1
    fibonacci(N,fibo)
    print(*fibo[N])
