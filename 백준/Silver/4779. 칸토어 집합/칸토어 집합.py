import sys
def K_set(str,num):
    if num==0:
        return str
    else:
        str = str + ' ' * len(str) + str
        return K_set(str,num-1)
while True:
    try:
        N=int(sys.stdin.readline())
        Str='-'
        print(K_set(Str,N))
    except:
        break