import sys
from collections import deque
def BFS(x,y):
    queue=deque([[x,y]]) # 시작 지점을 큐에 추가
    while queue: # 인접한 지점이 들어가 있는 큐
        x,y=queue.popleft() # 좌표를 방문하면 큐에서 삭제
        table[y][x]=0 # 방문 했으므로 1->0
        # 상하좌우, 대각선 4방향에 인접해있는지 확인
        for i in range(8):
            x2=x+dx[i]
            y2=y+dy[i]
            # 지도를 벗어나면 돌아온다.
            if x2<0 or x2>=w or y2<0 or y2>=h:
                continue
            # 방문한 좌표 인접한 좌표중 방문하지 않은 곳을
            # 큐에 추가한다.
            if table[y2][x2]==1:
                table[y2][x2]=0 # 방문 체크
                queue.append([x2, y2])
    return
    # while문을 빠져나왔다는 것은 더이상 인접한 곳에
    # 방문할 수 있는 곳이 없다는 것 (한 개의 섬 탐색이 끝남)

while True:
    w, h= map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    table=[]
    for i in range(h):
        table+=[list(map(int,sys.stdin.readline().split()))]
    cnt=0 # 섬의 개수

    # 상하좌우, 대각선 4방향 움직이는 좌표
    dx=[1,-1,0,0,1,1,-1,-1]
    dy=[0,0,1,-1,1,-1,1,-1]

    # 모든 좌표의 1(땅)인 부분을 들러서
    # 인접한 1을 다 돌면 섬의 개수 +1
    for y in range(h):
        for x in range(w):
            if table[y][x]==1:
                BFS(x,y) # 새로운 섬 탐색 시작
                cnt+=1
    print(cnt)