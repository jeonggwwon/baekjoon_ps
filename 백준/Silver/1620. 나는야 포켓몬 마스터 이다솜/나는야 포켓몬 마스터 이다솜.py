import sys
N,M=map(int,sys.stdin.readline().split())
dic={}
dic2={}
for i in range(N):
    a=sys.stdin.readline().rstrip()
    dic[a]=i+1
    dic2[i]=a
for i in range(M):
    p=sys.stdin.readline().rstrip()
    if p in dic:
        print(dic[p])
    else:
        print(dic2[int(p)-1])