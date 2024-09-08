import sys
N=int(sys.stdin.readline())
paper=[]
for i in range(N):
    paper+=[list(map(int, sys.stdin.readline().split()))]
cnt=[]
def QT(x,y,N):
    num=paper[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if num!=paper[i][j]:
                QT(x,y,N//3)
                QT(x+N//3,y,N//3)
                QT(x+2*N//3,y,N//3)

                QT(x,y+N//3,N//3)
                QT(x+N//3,y+N//3,N//3)
                QT(x+2*N//3,y+N//3,N//3)

                QT(x,y+2*N//3,N//3)
                QT(x+N//3,y+2*N//3,N//3)
                QT(x+2*N//3,y+2*N//3,N//3)
                return
    if num==0:
        cnt.append(0)
    elif num==1:
        cnt.append(1)
    else:
        cnt.append(-1)

QT(0,0,N)
print(cnt.count(-1))
print(cnt.count(0))
print(cnt.count(1))