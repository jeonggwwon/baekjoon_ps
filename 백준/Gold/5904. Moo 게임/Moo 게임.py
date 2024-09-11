import sys
n=int(sys.stdin.readline())
m_idx, i= 3, 3
while n>=m_idx:
    i+=1
    m_idx=m_idx*2+i

def moo(n,m_idx,i):
    if n<=(m_idx-i)//2:
        return moo(n,(m_idx-i)//2,i-1)
    elif (m_idx-i)//2<n<=((m_idx+i)//2):
        if n-(m_idx-i)//2==1:
            print('m')
            return
        else:
            print('o')
            return
    else:
        return moo(n-(m_idx-i)//2-i,(m_idx-i)//2,i-1)


moo(n,m_idx,i)