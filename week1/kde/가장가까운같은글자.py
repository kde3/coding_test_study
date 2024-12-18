def solution(s):
    answer = []
    
    D = {}
    for i, c in enumerate(s) :
        if D.get(c) != None :
            answer.append(i - D.get(c))
        else :
            answer.append(-1)
        D[c] = i
    
    return answer