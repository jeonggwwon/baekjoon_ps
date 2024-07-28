import sys
N=int(sys.stdin.readline())
arr=[]
for i in range(N):
    s=sys.stdin.readline().rstrip()
    s2=[len(s),s]
    if s2 not in arr:
        arr+=[s2]
arr.sort()
for i in range(len(arr)):
    print(arr[i][1])