import sys
sys.setrecursionlimit(10**5*6) #호출 깊이에 대한 설정
input = sys.stdin.readline

global sm
sm = 0
def dfs(cur,dpth,vis):
  global sm
  none = True
  for nxt in injup[cur]:
    if not vis[nxt]:
      none = False
      vis[nxt] = True
      dfs(nxt,dpth+1,vis)
  if none:
    sm += dpth

n = int(input())
injup = [[] for _ in range(n+1)]

for _ in range(n-1):
  s,e = map(int,input().split())
  injup[s].append(e)
  injup[e].append(s)
checked = [False for _ in range(n+1)]
checked[1] = True

dfs(1,0,checked)
if sm%2 == 1:
  print("Yes")
else:
  print("No")