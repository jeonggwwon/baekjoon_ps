import sys
R, C=map(int,sys.stdin.readline().split())
board=[]
for i in range(R):
    board+=[list(sys.stdin.readline().rstrip())]
res=[0]*26
maximum=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def back(x,y,res):
    global maximum
    for i in range(4):
        x2,y2=x+dx[i],y+dy[i]
        if 0<=x2<R and 0<=y2<C and res[ord(board[x2][y2])-65]==0:
            res[ord(board[x2][y2])-65]=res[ord(board[x][y])-65]+1
            back(x2,y2,res)
            res[ord(board[x2][y2])-65]=0
    if res[ord(board[x][y])-65] > maximum:
        maximum = res[ord(board[x][y])-65]
    return
res[ord(board[0][0])-65]=1
back(0,0,res)
print(maximum)