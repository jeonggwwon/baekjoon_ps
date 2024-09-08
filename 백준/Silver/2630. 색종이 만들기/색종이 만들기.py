import sys
N=int(sys.stdin.readline())
paper=[]
for i in range(N):
    paper+=[list(map(int,sys.stdin.readline().split()))]
num=[]
def QT(x,y,N):
    color=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color!=paper[i][j]:
                QT(x,y,N//2)
                QT(x+N//2,y,N//2)
                QT(x,y+N//2,N//2)
                QT(x+N//2,y+N//2,N//2)
                return
    if color==0:
        num.append(0)
    else:
        num.append(1)

QT(0,0,N)
print(num.count(0))
print(num.count(1))