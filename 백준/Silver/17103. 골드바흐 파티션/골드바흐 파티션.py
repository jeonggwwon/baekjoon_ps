import sys
import math
T=int(sys.stdin.readline())
for i in range(T):
    N=int(sys.stdin.readline())
    sum=N
    max = N
    prime = [1 for i in range(max + 1)]
    prime[1] = 0
    for i in range(2, int(math.sqrt(max)) + 1):
        if prime[i] == 1:
            j = 2
            while i * j <= max:
                prime[i * j] = 0
                j += 1
    sum = N
    num = 0
    for i in range(2, N - 1):
        if i==N/2+1:
            break
        if prime[i] == 1:
            if prime[sum - i] == 1:
                num += 1
            else:
                continue
    print(num)