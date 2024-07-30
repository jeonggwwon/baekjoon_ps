import sys
N=int(sys.stdin.readline())
N_arr=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
M_arr=list(map(int,sys.stdin.readline().split()))
result={}
for i in M_arr:
    result[i]=0
for i in N_arr:
    if i in result:
        result[i]+=1
for i in M_arr:
    print(result[i],end=' ')