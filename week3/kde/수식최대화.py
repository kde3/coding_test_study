from copy import deepcopy

def priority_calc(expression_list, p) :
    i = 0
    while len(expression_list) > 1 and i < len(expression_list) :
        if expression_list[i] == p :
            result = calc(expression_list[i-1], expression_list[i+1], p)
            expression_list[i-1:i+2] = [result]
            i -= 1
        i += 1

def calc(a, b, p) :
    a = int(a)
    b = int(b)
    
    if p == "+" :
        return a + b 
    elif p == "-" :
        return a - b
    elif p == "*" :
        return a * b
            
            
def solution(expression):
    priority_list = [
        ["+","-","*"],
        ["+","*","-"],
        ["-","+","*"],
        ["-","*","+"],
        ["*","+","-"],
        ["*","-","+"]
    ]    
    
    # 전처리
    expression_list = []
    s = ""
    for ex in expression :
        if ex == "+" or ex == "-" or ex == "*" :
            expression_list.append(s)
            expression_list.append(ex)
            s = ""
        else :
            s += ex
    expression_list.append(s)
    print(expression_list)
    
    # 계산
    result_list = []
    for priority in priority_list :
        expression_list_copy = deepcopy(expression_list)
        for p in priority :
            priority_calc(expression_list_copy, p)
        result_list.append(expression_list_copy[0])
            
    result_list = list(map(abs, result_list))
    return max(result_list)