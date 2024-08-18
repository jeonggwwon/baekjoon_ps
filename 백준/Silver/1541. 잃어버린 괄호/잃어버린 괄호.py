import sys
eq=sys.stdin.readline()
eq_L=[]
I=''
for i in eq:
    if i=='+' or i=='-':
        eq_L+=[I]
        I=''
        eq_L+=i
    elif i!='\n':
        I+=i
    if i=='\n':
        eq_L += [I]
sum=0
check=0
for i in eq_L:
    if i=='+':
        continue
    elif i=='-':
        check=1
        continue
    else:
        if check==0:
            sum+=int(i)
        elif check==1:
            sum-=int(i)
print(sum)