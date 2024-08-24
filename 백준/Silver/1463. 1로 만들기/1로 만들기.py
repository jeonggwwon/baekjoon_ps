import sys
N=int(sys.stdin.readline())
cnt=[0]*1000001
cnt[2], cnt[3]= 1, 1
if N>3:
    for i in range(4, N + 1):
        ele_1=cnt[i-1]
        next=ele_1
        if i%2==0:
            ele_2=cnt[i//2]
            if next>=ele_2:
                next=ele_2
        if i%3==0:
            ele_3=cnt[i//3]
            if next>=ele_3:
                next=ele_3
        cnt[i]=next+1
print(cnt[N])