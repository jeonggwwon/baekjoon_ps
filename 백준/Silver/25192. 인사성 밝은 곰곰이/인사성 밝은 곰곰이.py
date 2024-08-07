import sys
N=int(sys.stdin.readline())
member=set([])
p_num=0
for i in range(N):
    s=sys.stdin.readline().rstrip()
    if s=='ENTER':
        p_num+=len(member)
        member=set([])
        continue
    else:
        member.add(s)
p_num+=len(member)
print(p_num)