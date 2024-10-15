import sys
from collections import deque
n=int(sys.stdin.readline())
stair=deque([])
for i in range(n):
    stair+=[int(sys.stdin.readline())]
result=deque([])
for i in range(3):
    result.appendleft(0)
    stair.appendleft(0)
a,b=0,0
for i in range(3,n+3):
    a=result[i-3]+stair[i-1]+stair[i]
    b=result[i-2]+stair[i]
    result.append(max(a, b))
print(result[-1])