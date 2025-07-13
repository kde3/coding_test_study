from sys import stdin
input = stdin.readline

n, k = map(int,input().split())

inf = 10**9
dist = [[inf]*n for _ in range(n)]

for _ in range(k):
  s, e, l = map(int,input().split())
  dist[s-1][e-1] = l

for k in range(n):
  for i in range(n):
    for j in range(n):
      if dist[i][j] > dist[i][k] + dist[k][j]:
        dist[i][j] = dist[i][k] + dist[k][j]

ans = min([dist[i][i] for i in range(n)])
if ans >= inf:
  print(-1)
else:
  print(ans)


