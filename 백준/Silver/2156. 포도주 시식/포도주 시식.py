import sys
from collections import deque
n=int(sys.stdin.readline())
wine=deque([])
for i in range(n):
    wine+=[int(sys.stdin.readline())]
result=deque([])
for i in range(3):
    result.appendleft(0)
    wine.appendleft(0)
drink_1, drink_2, n_drink=0,0,0
for i in range(3,n+3):
    drink_1=result[i-3]+wine[i-1]+wine[i]
    drink_2=result[i-2]+wine[i]
    n_drink=result[i-1]
    result+=[max(n_drink,max(drink_1,drink_2))]
print(max(result))