import sys
N=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr2=list(set(arr))
arr2.sort()
dic={}
for i in range(len(arr2)):
    dic[arr2[i]]=i
result=[0]*N
for j in range(N):
    result[j]=dic[arr[j]]
print(*result)