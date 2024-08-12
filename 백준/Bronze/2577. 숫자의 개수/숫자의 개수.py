import sys
A=int(sys.stdin.readline())
B=int(sys.stdin.readline())
C=int(sys.stdin.readline())
p=A*B*C
arr=[0]*10
while True:
    if p<1:
        break
    arr[p%10]+=1
    p=p//10
for i in range(10):
    print(arr[i])