import sys
N=int(sys.stdin.readline())
num=0
check_start=0
check_end=0
L=[]
for i in range(N):
    L+=[list(map(int, sys.stdin.readline().split()))]
L.sort()
for i in range(N):
    if check_end>L[i][1] and check_start<=L[i][0]:
        check_end=L[i][1]
        check_start=L[i][0]
    elif check_end<=L[i][0]:
        num+=1
        check_end=L[i][1]
        check_start=L[i][0]
print(num)