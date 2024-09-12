import sys
N=int(sys.stdin.readline())
point=[[0]*100 for _ in range(100)]

for i in range(N):
    y,x=map(int,sys.stdin.readline().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            point[i][j]=1

area=0
for i in range(100):
    area+=point[i].count(1)

print(area)