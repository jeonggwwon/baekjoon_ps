import sys
K=int(sys.stdin.readline())
book=[]
check=0
sum=0
for i in range(K):
    cash=int(sys.stdin.readline())
    if cash==0:
        book.pop()
    else:
        book.append(cash)
if len(book)==0:
    print(0)
else:
    for i in book:
        sum+=i
    print(sum)