def solution(n, times):
    answer = 0
    times.sort()
    start, end = 0, times[-1]*n 
    
    while start<=end:
        cnt = 0
        mid=(start+end)//2
        
        for i in range(len(times)):
            cnt+=mid//times[i]
        if cnt>=n:
            answer=mid
            end=mid-1
        else:
            start=mid+1
    return answer