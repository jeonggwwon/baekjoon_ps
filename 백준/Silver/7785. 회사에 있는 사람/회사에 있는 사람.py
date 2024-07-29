import sys
n=int(sys.stdin.readline())
enter=set([])
for i in range(n):
    arr=list(sys.stdin.readline().split())
    if arr[1]=='enter':
        enter.add(arr[0])
    else:
        enter.remove(arr[0])
enter=list(enter)
enter.sort(reverse=True)
for i in range(len(enter)):
    print(enter[i])