import sys
N=int(sys.stdin.readline())
K=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
arr=list(set(arr))
if len(arr)>=K:
    arr.sort()
    dis = []
    for i in range(1, len(arr)):
        dis += [arr[i] - arr[i - 1]]
    dis.sort(reverse=True)
    result = 0
    for i in range(K-1):
        result+=dis[i]
    print(sum(dis) - result)
else:
    print(0)