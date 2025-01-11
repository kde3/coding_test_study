from collections import deque
def solution(board, moves):
    # 0. 전처리
    n = len(board)
    A = [deque() for _ in range(n+1)]
    
    for i in range(n) :
        for j in range(n) :
            if board[j][i] != 0 :
                A[i+1].append(board[j][i])
    
    # 1. 바구니에 다 담음.
    basket = []
    for m in moves :
        if A[m] :
            a = A[m].popleft()
            basket.append(a)
            
    # 2. 터뜨림(스택)
    answer = 0
    stack = []
    for b in basket :
        if stack and stack[-1] == b :
            stack.pop()
            answer += 1
        else :
            stack.append(b)
    
    return answer * 2