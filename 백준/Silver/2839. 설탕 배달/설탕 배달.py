import sys
N=int(sys.stdin.readline())
bag3, bag5=0,N//5
check=0
while True:
    if (5*bag5+3*bag3)==N:
        break
    if (N-(5*bag5+3*bag3))%3!=0:
        bag5-=1
        bag3+=1
        if bag5 <0:
            check = 1
            break
    else:
        bag3+=(N-(5*bag5+3*bag3))//3
if check==0:
    print(bag3+bag5)
else:
    print(-1)