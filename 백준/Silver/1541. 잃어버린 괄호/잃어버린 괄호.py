import sys
eq=sys.stdin.readline()
I=''
sum, check=0,0
for i in eq:
    if i!='-' and i!='+' and i!='\n':
        I += i
    else:
        if check == 1:
            sum -= int(I)
            I = ''
        else:
            sum += int(I)
            I = ''
        if i=='-':
            check=1
print(sum)