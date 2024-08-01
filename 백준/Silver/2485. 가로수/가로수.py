import sys
import math
def f_gcd(a,b):
    while b > 0:
        a,b = b,a % b
    return a

N=int(sys.stdin.readline())
point=[]
d=[]
for i in range(N):
    point+=[int(sys.stdin.readline())]
    if i==0:
        continue
    d+=[point[i]-point[i-1]]
d=list(set(d))
com = d[0]
for i in range(1, len(d)):
    com = f_gcd(com, d[i])

num=int(((point[len(point)-1]-point[0])/com)+1)
print(num-len(point))