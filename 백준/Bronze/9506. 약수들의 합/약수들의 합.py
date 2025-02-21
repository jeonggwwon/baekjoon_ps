import sys
while True:
    n = int(sys.stdin.readline())
    sum=0
    arr=[]
    if n==-1:
        break
    for i in range(1,n):
        if n%i==0:
            arr+=[i]
            sum+=i
    if n==sum:
        print(n,'=',end=' ')
        print(*arr,sep=' + ')
    else:
        print(f"{n} is NOT perfect.")