import sys
N,M=map(int,sys.stdin.readline().split())
dic={}
L=[]
for i in range(N):
    s=sys.stdin.readline().rstrip()
    if len(s)<M:
        continue
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
for i in dic:
    L+=[[dic[i],i]]
L=sorted(L,key=lambda x:(-x[0],-len(x[1]),x[1]))

for i in range(len(L)):
    print(L[i][1])