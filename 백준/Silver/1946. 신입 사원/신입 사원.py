import sys
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    app=[]
    for j in range(N):
        app+=[list(map(int,sys.stdin.readline().split()))]
    app.sort(key=lambda x:x[0])
    check, num = app[0][1],1
    for j in range(1,N):
        if app[j][1]<check:
            num+=1
            check=app[j][1]
    print(num)