from itertools import combinations
def solution(orders, course):
    answer = []
    
    for c in course :
        combi_dict = {}
        
        for o in orders :
            # c보다 조합할 수 있는 메뉴가 적으면 건너뜀.
            if len(o) < c :
                continue
            combi = combinations(o, c)
            for cb in combi :
                cb = list(cb)
                cb.sort()
                cb = "".join(cb)
                
                if combi_dict.get(cb) == None :
                    combi_dict[cb] = 1
                else :
                    combi_dict[cb] += 1
                    
        # 가장 많이 주문된 조합찾기
        if not combi_dict :
            continue
        max_val = max(combi_dict.values())
        if max_val == 1 :
            continue
        for k, v in combi_dict.items() :
            if v == max_val :
                answer.append(k)
    
    answer.sort()
    return answer