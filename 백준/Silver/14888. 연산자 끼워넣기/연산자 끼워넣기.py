import sys
N=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))
op=list(map(int,sys.stdin.readline().split()))
op2=[]
for i in range(4):
    for j in range(op[i]):
        op2+=[i]

max_n, min_n= -(10**9), 10**9
res=[]
def back():
    global max_n, min_n
    if len(res)==N-1:
        val=num[0]
        for j in range(N-1):
            if op2[res[j]]==0:
                val+=num[j+1]
            elif op2[res[j]]==1:
                val-=num[j+1]
            elif op2[res[j]]==2:
                val*=num[j+1]
            elif op2[res[j]]==3:
                if val>=0:
                    val//=num[j+1]
                else:
                    val=(abs(val)//num[j+1])*(-1)
        if val>max_n:
            max_n=val
        if val<min_n:
            min_n=val

    for i in range(N-1):
        if i not in res:
            res.append(i)
            back()
            res.pop()

    return

back()
print(max_n)
print(min_n)