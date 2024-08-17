import sys
N=int(sys.stdin.readline())
array=list(map(int,sys.stdin.readline().split()))
array.sort()
num=0
sum=0
for i in array:
    num+=i
    sum+=num
print(sum)