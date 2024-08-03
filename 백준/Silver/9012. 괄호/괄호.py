import sys
T=int(sys.stdin.readline())
for i in range(T):
    L,R=0,0
    PS=list(sys.stdin.readline().rstrip())
    Last=0
    while True:
        if PS[-1] == '(':
            L += 1
            Last=0
            PS.pop()
        elif PS[-1]==')':
            R += 1
            Last=1
            PS.pop()
        if L == R and Last==0:
            L, R = 0, 0
        elif L==R and Last==1:
            break
        if len(PS)==0:
            break

    if L == 0 and R == 0:
        print('YES')
    else:
        print('NO')