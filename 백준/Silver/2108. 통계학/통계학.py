import sys
N=int(sys.stdin.readline())
sum=0
L=[]
dic={}
for i in range(N):
    num=int(sys.stdin.readline())
    sum+=num
    L+=[num]
    if num in dic:
        dic[num]+=1
    else:
        dic[num]=0
result=sum/N
print(int(round(result,0)))
L.sort()
print(L[N//2])
max=-1
idx=[]
for i in dic:
    if dic[i]>max:
        max=dic[i]
        idx=[i]
    elif dic[i]==max:
        idx+=[i]
if len(idx)>1:
    idx.sort()
    print(idx[1])
else:
    print(idx[0])
print(L[N-1]-L[0])