import sys
N, L=map(int,sys.stdin.readline().split())
stu=0
max=1
while stu<N:
    while True:
        if str(L) in list(str(max)):
            max+=1
        else:
            stu+=1
            break
    max += 1
print(max-1)