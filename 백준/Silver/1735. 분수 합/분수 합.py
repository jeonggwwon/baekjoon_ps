import sys
A1,B1=map(int,sys.stdin.readline().split())
A2,B2=map(int,sys.stdin.readline().split())
A= (A1*B2)+(A2*B1)
B= B1*B2

com=1
for i in range(B,0,-1):
    if A%i==0 and B%i==0:
        com=i
        break
    else:
        com-=1

print(int(A/com),int(B/com))