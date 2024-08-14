import sys
def hanoi(N,op,ed):
    if N==1:
        print(op,ed,sep=' ')
        return
    else:
        hanoi(N-1,op,6-(op+ed))
        print(op,ed,sep=' ')
        hanoi(N-1,6-(op+ed),ed)

N=int(sys.stdin.readline())
print(2**N-1)
hanoi(N,1,3)
