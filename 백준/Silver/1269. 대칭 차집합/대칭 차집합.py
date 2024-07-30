import sys
A,B=map(int,sys.stdin.readline().split())
A_arr=list(sys.stdin.readline().split())
B_arr=list(sys.stdin.readline().split())
A_B=set(A_arr)-set(B_arr)
B_A=set(B_arr)-set(A_arr)
result=A_B|B_A
print(len(result))