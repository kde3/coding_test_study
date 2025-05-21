from collections import deque
def bfs(y,x,visit,ln):
  dy = [1,-1,0,0]
  dx = [0,0,-1,1]
  q = deque([(y,x)])
  while q:
    y,x = q.popleft()
    for k in range(4):
      ny = y + dy[k]
      nx = x + dx[k]
      if not (0 <= ny < ln and 0 <= nx < ln):
        continue
      if visit[ny][nx]:
        continue
      visit[ny][nx] = True
      q.append((ny,nx))
  return visit

n = int(input())
board = []
pool = []
for _ in range(n):
  tmp = list(map(int,input().split(" ")))
  board.append(tmp)
  pool.extend(tmp)

pool = sorted(list(set(pool)))
ans = 1
for level in pool:
  cnt = 0
  vis = [[False if board[i][j] >= level else True for j in range(n)]for i in range(n)]
  for i in range(n):
    for j in range(n):
      if not vis[i][j]:
        cnt += 1
        vis = bfs(i,j,vis,n)
  ans = max(ans,cnt)

print(ans)