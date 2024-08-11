import sys
def star(s1,s2,idx,N):
    s=s1+s2+s1
    if N==idx:
        return s1+s2+s1
    else:
        return star(star1(s,idx*3),star2(s,idx*3),idx*3,N)
def star1(s,idx):
    temp=s
    s=''
    for i in range(0,int(idx/3)):
        s+=temp[i*int(idx/3):i*int(idx/3)+int(idx/3)]*3
    return s
def star2(s,idx):
    temp=s
    s=''
    for i in range(0, int(idx/3)):
        s += temp[i*int(idx/3):i*int(idx/3)+int(idx/3)]+' '*int(idx/3)+temp[i*int(idx/3):i*int(idx/3)+int(idx/3)]
    return s
N=int(sys.stdin.readline())
s='*'
result=star(star1(s,3),star2(s,3),3,N)
for i in range(N):
    print(result[i*N:i*N+N])