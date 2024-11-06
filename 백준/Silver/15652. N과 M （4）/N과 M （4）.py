import sys
N,M=map(int,sys.stdin.readline().split())
res=[]

def back(start):
    if len(res)==M:
        print(*res)
        return
    for i in range(start,N+1):
        res.append(i)
        back(i)
        res.pop()

back(1)