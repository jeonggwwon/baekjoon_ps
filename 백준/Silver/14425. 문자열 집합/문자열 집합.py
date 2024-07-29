import sys
N,M=map(int, sys.stdin.readline().split())
NL=[]
ML=[]
num=0
for i in range(N):
    NL+=[sys.stdin.readline().rstrip()]
for i in range(M):
    ML=sys.stdin.readline().rstrip()
    if ML in set(NL):
        num+=1
print(num)