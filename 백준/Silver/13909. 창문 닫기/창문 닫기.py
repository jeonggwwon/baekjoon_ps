import sys
import math
N=int(sys.stdin.readline())
num=0
for i in range(1,N+1):
    if N>=i**2:
        num+=1
    else:
        break
print(num)