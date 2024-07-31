import sys
A, B=map(int, sys.stdin.readline().split())
dic_a={}
Test_a = A
for a in range(2,A+1):
    while Test_a%a==0:
        if a in dic_a:
            dic_a[a]+=1
        else:
            dic_a[a]=1
        Test_a=Test_a/a
dic_b={}
Test_b = B
for b in range(2,B+1):
    while Test_b%b==0:
        if b in dic_b:
            dic_b[b] += 1
        else:
            dic_b[b] = 1
        Test_b=Test_b/b
arr=[]
for i in dic_a:
    if i in dic_b:
        if dic_a[i] > dic_b[i]:
            arr += [i] * dic_a[i]
        else:
            arr += [i] * dic_b[i]
    else:
        arr += [i] * dic_a[i]
for i in dic_b:
    if i not in dic_a:
        arr += [i] * dic_b[i]
com=1
for i in range(len(arr)):
    com*=arr[i]
print(com)