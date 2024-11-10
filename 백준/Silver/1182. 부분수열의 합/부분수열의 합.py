import sys
N, S=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

res=[]
cnt=0
def back(start):
    global cnt
    if len(res)>0 and sum(res)==S:
        cnt+=1

    for i in range(start, N):
        res.append(arr[i])
        back(i + 1)
        res.pop()

    return cnt
print(back(0))