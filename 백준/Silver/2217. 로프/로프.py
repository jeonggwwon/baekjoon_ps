import sys
N=int(sys.stdin.readline())
rope=[]
for i in range(N):
    rope+=[int(sys.stdin.readline())]
rope.sort(reverse=True)
result=[]
for i in range(N,0,-1):
    result+=[rope.pop()*i]
print(max(result))