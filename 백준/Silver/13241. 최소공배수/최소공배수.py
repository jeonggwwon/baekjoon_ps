import sys
A, B=map(int, sys.stdin.readline().split())
if A>B:
    a,b=A,B
else:
    a,b=B,A
com=1
for i in range(b,0,-1):
    if a%i==0 and b%i==0:
        com=i
        break
    else:
        com-=1
print(int(A*B/com))