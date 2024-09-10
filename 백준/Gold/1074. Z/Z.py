import sys
N,r,c=map(int,sys.stdin.readline().split())
L=2**N
def Z(L,r,c,tmp):
    if L==2:
        print(2*r+c+tmp)
        return

    if r<L//2 and c<L//2: #1
        Z(L//2,r,c,tmp)
    elif r<L//2 and c>=L//2: #2
        Z(L//2,r,c-(L//2),tmp+((L//2)**2)*1)
    elif r>=L//2 and c<L//2: #3
        Z(L//2,r-(L//2),c,tmp+((L//2)**2)*2)
    elif r>=L//2 and c>=L//2: #4
        Z(L//2,r-(L//2),c-(L//2),tmp+((L//2)**2)*3)

Z(L,r,c,0)