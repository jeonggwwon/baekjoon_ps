def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance)
    rocks.sort()
    start, end= 0, rocks[-1]
    
    while start<=end:
        cnt, cur= 0, 0
        mid=(start+end)//2
        for i in range(len(rocks)):
            if rocks[i]-cur<mid:
                cnt+=1
            else:
                cur=rocks[i]
        if cnt>n:
            end=mid-1
        else:
            answer=mid
            start=mid+1
    return answer