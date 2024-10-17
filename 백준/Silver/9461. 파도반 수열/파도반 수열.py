import sys
T=int(sys.stdin.readline())
ln=[]
for i in range(T):
    ln+=[int(sys.stdin.readline())]
for length in ln:
    result = [1, 1, 1, 2, 2]
    if length>5:
        for i in range(length-5):
            result+=[result[-1]+result[i]]
    print(result[length-1])