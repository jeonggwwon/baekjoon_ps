import sys
N,M=map(int,sys.stdin.readline().split())
N_arr=[]
M_arr=[]
for i in range(N):
    N_arr+=[sys.stdin.readline().rstrip()]
for i in range(M):
    M_arr+=[sys.stdin.readline().rstrip()]
result=set(N_arr)&set(M_arr)
result=list(result)
result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])