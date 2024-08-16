import sys
N, K=map(int,sys.stdin.readline().split())
array=[]
for i in range(N):
    A=int(sys.stdin.readline())
    if A>K:
        continue
    array += [A]
num=0
for i in range(len(array)-1,-1,-1):
    num+=K//array[i]
    K=K%array[i]
    if K==0:
        break
print(num)