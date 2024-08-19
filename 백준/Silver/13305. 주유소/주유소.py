import sys
N=int(sys.stdin.readline())
city_len=list(map(int,sys.stdin.readline().split()))
city_sum=0
for i in range(N-1):
    city_sum+=city_len[i]
L_price=list(map(int,sys.stdin.readline().split()))
min=L_price[0]*city_sum
check=L_price[0]
for i in range(1,N-1):
    if L_price[i]<check:
        city_sum-=city_len[i-1]
        min-=check*city_sum
        check=L_price[i]
        min+=check*city_sum
    else:
        city_sum -= city_len[i-1]
        pass
print(min)