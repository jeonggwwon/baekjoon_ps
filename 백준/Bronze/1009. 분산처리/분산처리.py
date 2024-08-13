import sys
T=int(sys.stdin.readline())
for i in range(T):
    a,b=map(int,sys.stdin.readline().split())
    array=[]
    for j in range(1,5):
        num=(a**j)%10
        if num==0:
            num=10
        array+=[num]
    print(array[b%4-1])