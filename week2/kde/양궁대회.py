'''
어피치가 점수 못 얻도록 라이언이 더 많이 맞춰야 함.

- 큰 과녁 점수 못가져가도록 하는 것도 좋은데 큰거 냅두고 나머지 맞춰도 이길 수도(10 vs 9+8) => ㅇㅇ
- 어피치가 0발 쏜 것도 라이언은 1발만 쏘면 점수 가져감.


라이언이 가장 큰 점수 차이로 우승할 수 있는 방법이 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요.
'''
from copy import deepcopy
INF = int(1e9)
# 점수 계산
def calc(A) :
    result = 0
    for i, a in enumerate(A) :
        if a != 0 :
            result += 10 - i
    return result

def dfs(n, info, i, score, answer) :
    if i == 11 :
        if sum(answer) < n :
            answer[-1] = n - sum(answer)
        return answer, score
    if sum(answer) >= n :
        return answer, score
    
    Y = [-1]
    Y_result = -INF
    # Y(n이 해당 어피치가 쏜 것보다 많아야 Y 가능.)
    if n - sum(answer) > info[i] :
        # 어피치가 0발 이면 점수를 그냥 더함.
        # 어피치의 점수를 뺏은 거면 점수차는 *2가 되므로 *2해서 더함.
        if info[i] == 0 :
            Y_score = score + (10 - i)
        else :
            Y_score = score + (10 - i)*2
        Y_answer = deepcopy(answer)
        Y_answer[i] = info[i] + 1
        Y, Y_result = dfs(n, info, i+1, Y_score, Y_answer)
    
    # N
    N_result = -INF
    N, N_result = dfs(n, info, i+1, score, answer)
    
    if Y_result > N_result :
        return Y, Y_result
    elif Y_result < N_result :
        return N, N_result
    else :
        for i in range(11, -1, -1) :
            if sum(Y[i:]) > sum(N[i:]) :
                return Y, Y_result
            elif sum(Y[i:]) < sum(N[i:]) :
                return N, N_result
        
    return [-1], -INF


def solution(n, info):
    answer = [0] * 11
    answer, t = dfs(n, info, 0, -calc(info), answer)
    if t <= 0 :
        return [-1]
    return answer