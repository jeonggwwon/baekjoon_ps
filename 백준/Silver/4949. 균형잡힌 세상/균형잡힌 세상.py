import sys
while True:
    s=list(sys.stdin.readline().rstrip())
    if s[0]=='.':
        break
    s.pop()
    start_stack=[]
    check=0
    while True:
        if s[-1] == '(':
            if len(start_stack)==0:
                check=1
                break
            if start_stack[-1]==')':
                start_stack.pop()
                s.pop()
            else:
                check=1
                break
        elif s[-1] == ')':
            start_stack+=[')']
            s.pop()
        elif s[-1]=='[':
            if len(start_stack)==0:
                check=1
                break
            if start_stack[-1]==']':
                start_stack.pop()
                s.pop()
            else:
                check=1
                break
        elif s[-1]==']':
            start_stack+=[']']
            s.pop()
        else:
            s.pop()
        if len(s)==0:
            break
    if len(start_stack)>0 or check==1:
        print('no')
    elif len(start_stack)==0 and check==0:
        print('yes')