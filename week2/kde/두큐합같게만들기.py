from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    n = len(queue1) + len(queue2)
    answer = 0
    
    for _ in range(n*2 + 5) :
        if s1 > s2 :
            q = queue1.popleft()
            queue2.append(q)
            s1 -= q
            s2 += q
        elif s1 < s2 :
            q = queue2.popleft()
            queue1.append(q)
            s1 += q
            s2 -= q
        else :
            return answer
        answer += 1
    
    return -1