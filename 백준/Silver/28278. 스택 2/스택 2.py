import sys
N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    cmd =list(map(int,sys.stdin.readline().split()))
    if cmd[0]==1:
        stack.append(cmd[1])
    elif cmd[0]==2:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif cmd[0]==3:
        print(len(stack))
    elif cmd[0]==4:
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif cmd[0]==5:
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])