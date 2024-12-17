import sys
from collections import deque
N=int(sys.stdin.readline())
arr= deque([])
cnt=0
for i in range(N):
    #heapq.heappush(arr,int(sys.stdin.readline()))
    arr.append(int(sys.stdin.readline()))
    if arr[-1]<0:
        cnt+=1
if N==1:
    print(arr[0])
else:
    result=0
    arr=list(arr)
    arr.sort()
    arr=deque(arr)
    while len(arr)>0:
        if cnt>1:
            temp1=arr.popleft()
            temp2=arr.popleft()
            cnt-=2
            result+= (temp1*temp2)
        else:
            if cnt==1:
                temp=arr.popleft()
                if len(arr)>0:
                    if arr[0]==0:
                        temp*=arr.popleft()
                result+=temp
                cnt-=1
            else:
                if arr[0]==0:
                    arr.popleft()
                    continue
                if arr[0]==1:
                    result+=arr.popleft()
                    continue
                arr = list(arr)
                arr.sort(reverse=True)
                arr = deque(arr)
                if len(arr)>1:
                    temp1=arr.popleft()
                    temp2=arr.popleft()
                    result+=(temp1*temp2)
                else:
                    result+=arr.popleft()
    print(result)