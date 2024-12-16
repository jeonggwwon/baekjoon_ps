import sys
import heapq
N=int(sys.stdin.readline())
c=[]
for i in range(N):
   heapq.heappush(c,int(sys.stdin.readline()))
result=0
while len(c)>1:
    temp1=heapq.heappop(c)
    temp2=heapq.heappop(c)
    result+=temp1+temp2
    heapq.heappush(c,temp1+temp2)
print(result)