import sys
S=sys.stdin.readline().rstrip()
part=[]
for i in range(len(S)):
    for j in range(len(S)):
        part+=[S[i:i+j+1]]
part=set(part)
print(len(part))