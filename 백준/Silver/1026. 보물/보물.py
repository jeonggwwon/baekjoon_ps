import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
B=list(map(int,sys.stdin.readline().split()))
A_arr=sorted(A)
B_arr=sorted(B,reverse=True)
s=0
for i in range(N):
    s+=A_arr[i]*B_arr[i]
print(s)