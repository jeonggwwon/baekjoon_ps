import sys
money=int(sys.stdin.readline())
money=1000-money
num=0
arr=[500,100,50,10,5,1]
for i in range(6):
    if money==0:
        break
    else:
        num+=money//arr[i]
        money%=arr[i]
print(num)