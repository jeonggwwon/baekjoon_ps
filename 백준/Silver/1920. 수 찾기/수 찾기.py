import sys
N=int(sys.stdin.readline())
A=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
target=list(map(int,sys.stdin.readline().split()))

def binary_search(target,data):
    start=0
    end=len(data)-1

    while start<=end:
        mid=(start+end)//2
        if data[mid]==target:
            return 1
        elif data[mid]>target:
            end=mid-1
        elif data[mid]<target:
            start=mid+1
    return 0

A.sort()

for i in target:
    print(binary_search(i,A))