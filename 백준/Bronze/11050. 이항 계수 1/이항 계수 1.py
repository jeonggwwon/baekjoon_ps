import sys
N,K=map(int,sys.stdin.readline().split())
N_P=1
K_P=1
P=1
for i in range(N,0,-1):
    N_P*=i
for i in range(K,0,-1):
    K_P*=i
for i in range(N-K,0,-1):
    P*=i
print(int(N_P/(K_P*P)))