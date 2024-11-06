import sys
N,M=map(int,sys.stdin.readline().split())
res=[0]

def back():
    if len(res)==M+1:
        print(*res[1:M+1])
        return
    for i in range(res[-1]+1,N+1):
        if i not in res:
            res.append(i)
            back()
            res.pop()

back()