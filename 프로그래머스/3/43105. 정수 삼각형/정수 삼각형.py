def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        triangle[i][0]+=triangle[i-1][0]
        triangle[i][i]+=triangle[i-1][i-1]
        for j in range(1,i):
            if triangle[i-1][j-1]>triangle[i-1][j]:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=triangle[i-1][j]
    triangle[len(triangle)-1].sort(reverse=True)
    answer=triangle[len(triangle)-1][0]
    return answer