import sys
n=int(sys.stdin.readline())
def fib(n):
    global num1
    if n==1 or n==2:
        return 1
    else:
        num1 += 1
        return fib(n-1)+fib(n-2)

def fibonacci(n):
    global num2
    f[1], f[2]= 1, 1
    for i in range(3,n+1):
        num2+=1
        f[i]=f[i-1]+f[i-2]
    return f[n]

f=[0]*(n+1)

num1, num2= 1, 0
fib(n)
fibonacci(n)
print(num1, num2)