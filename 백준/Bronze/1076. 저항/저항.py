import sys
arr=[]
for i in range(3):
    arr+=[sys.stdin.readline().rstrip()]
result=0
check=0
for i in range(3):
    if arr[i]=='black':
        check=0
    elif arr[i]=='brown':
        check=1
    elif arr[i]=='red':
        check=2
    elif arr[i]=='orange':
        check=3
    elif arr[i]=='yellow':
        check=4
    elif arr[i]=='green':
        check=5
    elif arr[i]=='blue':
        check=6
    elif arr[i]=='violet':
        check=7
    elif arr[i]=='grey':
        check=8
    elif arr[i]=='white':
        check=9

    if i==0:
        result+=check
    elif i==1:
        result*=10
        result+=check
    else:
        result*=(10**check)
print(result)