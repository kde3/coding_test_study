#그래프를 합병하는 과정

# n = int(input())

# edges = {}
# for _ in range(n):
#   s,e,l = input().split()
#   l = int(l)
#   if edges.get((s,e)) == None:
#     edges[(s,e)] = [l]
#   else:
#     edges[(s,e)].append(l)

# print(edges)


import sys
from collections import deque
input = sys.stdin.readline

# 0–25: A–Z, 26–51: a–z # 문자를 숫자로 바꾸는 함수
def char_to_idx(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

N = int(input())  # 파이프 수
MAX = 52  # 총 노드 수 (A–Z + a–z)
capacity = [[0]*MAX for _ in range(MAX)] # 흐를수 있는 최대 양 (처음엔 입력값만큼)
adj = [[] for _ in range(MAX)] # 연결된 노드등 저장 

# 파이프 정보 입력
for _ in range(N):
    u, v, w = input().split()
    w = int(w)
    u, v = char_to_idx(u), char_to_idx(v)
    capacity[u][v] += w
    capacity[v][u] += w
    adj[u].append(v)
    adj[v].append(u)

def edmonds_karp(s, t):
    flow = 0
    parent = [-1]*MAX

    while True: # 4. 더이상 경로가 없을때까지 반복 
        for i in range(MAX):
            parent[i] = -1
        parent[s] = s
        q = deque([s])

        # 1. BFS로 (증가 경로 탐색) 
        while q and parent[t] == -1:
            cur = q.popleft()
            for nxt in adj[cur]:
                if parent[nxt] == -1 and capacity[cur][nxt] > 0:
                    parent[nxt] = cur
                    q.append(nxt)
        print(parent)
        # A→Z 경로 없으면 종료
        if parent[t] == -1:
            break

        # 2. 경로에서 흐를 수 있는 최소 용량 찾기
        amount = float('inf')
        v = t
        while v != s:
            u = parent[v]
            amount = min(amount, capacity[u][v])
            v = u

        # 3. 흐르고 나면 잔여 용량 업데이트
        v = t
        while v != s:
            u = parent[v]
            capacity[u][v] -= amount
            capacity[v][u] += amount
            v = u

        flow += amount

    return flow

# 결과 출력 (A=0, Z=25)
print(edmonds_karp(0, 25))



