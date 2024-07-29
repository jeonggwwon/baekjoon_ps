import sys
N=int(sys.stdin.readline())
N_arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
M_arr=list(map(int,sys.stdin.readline().split()))
result={}
for i in M_arr:
    result[i]=0
arr=list(set(N_arr)&set(M_arr))
for i in arr:
    result[i]=1
for i in M_arr:
    print(result[i],end=' ')