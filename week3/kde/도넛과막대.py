def solution(edges):
    edges_count = {}
    for a, b in edges :
        if not edges_count.get(a) == None :
            edges_count[a] = [0, 0]
        if not edges_count.get(b) == None :
            edges_count[b] = [0, 0]
    
        edges_count.get(a)[0] += 1
        edges_count.get(b)[1] += 1
        
    # print(edges_count)
        
    answer = [0, 0, 0, 0]
    for k, [a, b] in edges_count.items() :
        if a >= 2 and b == 0 :
            answer[0] = k
        elif a == 0 and b >= 1 :
            answer[2] += 1
        elif a >= 2 and b >= 2 :
            answer[3] += 1
    
    answer[1] = edges_count.get(answer[0])[0] - answer[2] - answer[3]
    
    return answer