from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    people=deque(people)
    print(people)
    while True:
        if len(people)==0:
            break
        elif len(people)==1:
            answer+=1
            break
        else:
            if people[-1]+people[0]<=limit:
                answer+=1
                people.pop()
                people.popleft()
            else:
                answer+=1
                people.pop()
    return answer