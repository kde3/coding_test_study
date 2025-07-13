import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(2*(10**5))

n, r, q = map(int,input().split())
injup = [[] for _ in range(n+1)]
for _ in range(n-1):
  s,e = map(int,input().split())
  injup[s].append(e)
  injup[e].append(s)

subtree_size = [0] * (n + 1)

#dfs에 넣을 수 있는 요소가 무엇이 있는가... 생각 좀 해봐야겠네
def dfs(node, parent):
    size = 1 
    for nei in injup[node]:
        if nei != parent: 
            size += dfs(nei, node)
    subtree_size[node] = size
    return size

dfs(r,-1)
ans = []
for _ in range(q):
    ans.append(subtree_size[int(input())])

for a in ans:
    print(a)

# q = deque([r])
# vis = [False for _ in range(n+1)]
# vis[r] = True
# while q:
#   tmp = q.popleft()
#   gets = [e if s == tmp else s for s,e in edges if tmp in (s,e)]
#   for nxt in gets:
#     if vis[nxt]:
#       continue

