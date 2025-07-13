from sys import stdin
input = stdin.readline

def check(N,edges):
  inf = 10**9
  dist = [inf]*N
  dist[0] = 0
  for _ in range(n-1):
    for s,e,l in edges:
      if dist[e-1] >  dist[s-1] + l:
        dist[e-1] =  dist[s-1] + l
  for s,e,l in edges:
      if dist[e-1] >  dist[s-1] + l:
        return "YES"
  return "NO"

t = int(input())
ans = []
for _ in range(t):
  n,k,w = map(int,input().split())
  edges = []
  for i in range(k+w):
    s,e,l = map(int,input().split())
    if i < k:
      edges.append((s,e,l))
      edges.append((e,s,l))
    else:
      edges.append((s,e,-l))
  ans.append(check(n,edges))

for a in ans:
  print(a)