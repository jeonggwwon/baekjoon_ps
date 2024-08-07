import sys
N=int(sys.stdin.readline())
rainbow=set(['ChongChong'])
for i in range(N):
    p1,p2=sys.stdin.readline().split()
    if rainbow & set([p1]) and not (rainbow & set([p2])):
        rainbow.add(p2)
    elif not(rainbow & set([p1])) and rainbow & set([p2]):
        rainbow.add(p1)
print(len(rainbow))