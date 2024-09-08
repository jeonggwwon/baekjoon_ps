import sys
N=int(sys.stdin.readline())
num=[]
for i in range(N):
    num+=[list(map(int,sys.stdin.readline().split()))]
result=[]
def QT(x,y,N):
    for i in range(x,x+N):
        for j in range(y,y+N):
            c1 = QT(x, y, N // 2)
            c2 = QT(x + N // 2, y, N // 2)
            c3 = QT(x, y + N // 2, N // 2)
            c4 = QT(x + N // 2, y + N // 2, N // 2)
            result=[c1,c2,c3,c4]
            result.sort()
            return result[1]
    return num[x][y]

print(QT(0,0,N))