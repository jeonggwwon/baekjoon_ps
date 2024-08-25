import sys
n=int(sys.stdin.readline())
tri=[]
input=[]
for i in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    if i==0:
        tri=input
        continue
    input[0]+=tri[0]
    input[len(input)-1]+=tri[len(input)-2]
    for j in range(1,len(input)-1):
        if tri[j-1]>tri[j]:
            input[j]+=tri[j-1]
        else:
            input[j]+=tri[j]
    tri=input
tri.sort(reverse=True)
print(tri[0])