import sys
N,m,M,T,R=map(int,sys.stdin.readline().split())
x=m
time=0
health=0
if m+T>M:
    time=-1
else:
    while health < N:
        if x + T <= M:
            x += T
            health += 1
        elif x - R >= m:
            x -= R
        elif x - R < m:
            x = m
        time += 1

print(time)