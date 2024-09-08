import sys
N=int(sys.stdin.readline())
media=[]
for i in range(N):
    media+=[list(map(int,sys.stdin.readline().rstrip()))]
result=[]
def QT(x,y,N):
    bit=media[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if bit != media[i][j]:
                result.append('(')
                QT(x, y, N // 2)
                QT(x, y + N // 2, N // 2)
                QT(x + N // 2, y, N // 2)
                QT(x + N // 2, y + N // 2, N // 2)
                result.append(')')
                return
    if bit == 0:
        result.append(0)
    else:
        result.append(1)
QT(0,0,N)
print(*result,sep='')