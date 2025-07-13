#간단한 bfs

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,m = map(int,input().split())


board = []
for _ in range(m):
  board.append(list(input())[0:n]) #/n도 같이 들어가네
vis = [[False for _ in range(n)] for _ in range(m)]

q = deque([])
ans = [0,0]
for y in range(m):
  for x in range(n):
    if not vis[y][x]:
      cnt = 0
      alp = board[y][x]
      q.append((y,x))
      while q:
        tmp = q.popleft()
        cnt += 1
        vis[tmp[0]][tmp[1]] = True
        for i in range(4):
          ny = tmp[0]+dy[i]
          nx = tmp[1]+dx[i]
          if ny < 0 or ny >= m  or nx < 0 or nx >= n:
            continue
          if not vis[ny][nx] and alp == board[ny][nx] and not (ny,nx) in q:
            q.append((ny,nx))
      if alp == "B":
        ans[1] += cnt**2
      else:
        ans[0] += cnt**2

print(" ".join(map(str,ans)))