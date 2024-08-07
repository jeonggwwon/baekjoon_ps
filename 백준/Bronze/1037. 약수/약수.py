import sys
num=int(sys.stdin.readline())
factor=list(map(int,sys.stdin.readline().split()))
N=1
if num==1:
    N=factor[0]*factor[0]
else:
    factor.sort()
    N=factor[0]*factor[num-1]
print(N)