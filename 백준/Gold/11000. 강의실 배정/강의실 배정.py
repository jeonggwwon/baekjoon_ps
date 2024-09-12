import sys
import heapq
N=int(sys.stdin.readline())
Class=[]
for i in range(N):
    Class+=[list(map(int, sys.stdin.readline().split()))]
Class.sort(key= lambda x:(x[0], x[1]))

res=[]
heapq.heappush(res, Class[0][1])
for i in range(1,N):
    if Class[i][0]<res[0]:
        heapq.heappush(res,Class[i][1])
    else:
        heapq.heappop(res)
        heapq.heappush(res,Class[i][1])
print(len(res))