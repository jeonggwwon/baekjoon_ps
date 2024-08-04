import sys
N=int(sys.stdin.readline())
stack=list(map(int,sys.stdin.readline().split()))
order=1
stand=[]
check=0
while True:
    if len(stack)>0:
        if len(stand)==0:
            if order==stack[0]:
                stack.pop(0)
                order+=1
            else:
                stand+=[stack[0]]
                stack.pop(0)
        else:
            if order==stack[0]:
                stack.pop(0)
                order+=1
            elif order==stand[-1]:
                stand.pop()
                order+=1
            else:
                stand += [stack[0]]
                stack.pop(0)
    else:
        if len(stand)>0:
            if order==stand[-1]:
                stand.pop()
                order+=1
            else:
                check=1
                break
        else:
            break
if check==1:
    print('Sad')
else:
    print('Nice')