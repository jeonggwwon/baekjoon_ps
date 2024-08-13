import sys
import math
A,B,C=map(int,sys.stdin.readline().split())
num=1
while True:
    if C <= B:
        print(-1)
        break
    else:
        num=int(A/(C-B))+1
        print(num)
        break