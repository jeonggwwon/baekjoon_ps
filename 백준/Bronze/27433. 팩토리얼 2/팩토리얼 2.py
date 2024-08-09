import sys
N=int(sys.stdin.readline())
p=1
for i in range(N,0,-1):
    p*=i
print(p)