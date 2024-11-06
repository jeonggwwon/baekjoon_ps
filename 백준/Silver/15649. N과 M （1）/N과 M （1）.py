import sys
N,M=map(int,sys.stdin.readline().split())
res=[]

def back():
    if len(res)==M:
        print(*res)
        return
    for i in range(1,N+1):
        if i not in res:
            res.append(i)
            back()
            res.pop()

back()