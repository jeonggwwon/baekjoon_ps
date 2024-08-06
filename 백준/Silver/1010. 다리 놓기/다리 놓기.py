import sys
T=int(sys.stdin.readline())
for j in range(T):
    N,M=map(int,sys.stdin.readline().split())
    N_P = 1
    M_P = 1
    P = 1
    for i in range(N, 0, -1):
        N_P *= i
    for i in range(M, 0, -1):
        M_P *= i
    for i in range(M-N, 0, -1):
        P *= i
    print(int(M_P / (N_P * P)))