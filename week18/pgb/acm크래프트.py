# t = int(input())
# ans = []
# for _ in range(t):
#   n,k = map(int,input().split())
#   tm = list(map(int,input().split()))
#   injup_rev = [[0] for _ in range(n)]
#   injup = [[0] for _ in range(n)]
#   for _ in range(k):
#     s,e = map(int,input().split())
#     injup[s-1].append(e)
#     injup_rev[e-1].append(s)
  
#   dest = int(input())
#   start = injup_rev.index([0])+1

#   vis = [False]*n
#   dist = [0]*n
#   cur = start
#   dist[start-1] = tm[start-1]
#   while list(set(vis)) != [True]:
#     for nxt in injup[cur-1]:
#       if nxt == 0:
#         continue
#       dist[nxt-1] = max(dist[cur-1]+tm[nxt-1],dist[nxt-1])
#     vis[cur-1] = True
#     cur = 0
#     for i in range(n):
#       if vis[i]:
#         continue
#       if dist[i] == 0:
#         continue
#       if cur < dist[i]:
#         cur = i+1
#   ans.append(dist[dest-1])
#   print(f'요 테스트 답 : {dist[dest-1]}')
# for a in ans:
#   print(a)

#import heapq
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
ans = []
for _ in range(N):
  n,k = map(int,input().split())
  ans_pool = [-1]*(n+1)
  fin = [0]*(n+1)
  link = [[] for _ in range(n+1)]
  link_rev = [[] for _ in range(n+1)]

  tms = list(map(int,input().split()))
  for _ in range(k):
    s,e = map(int,input().split())
    link[s].append(e)
    link_rev[e].append(s)
    fin[e] += 1
  dest = int(input())

  h = deque([i for i in range(1,n+1) if fin[i] == 0])
  while ans_pool[dest] == -1:
    tmp = h.popleft()
    if ans_pool[tmp] != -1:
      continue
    tm = 0
    for x in link_rev[tmp]:
      if ans_pool[x] > tm:
        tm = ans_pool[x]
    ans_pool[tmp] = tm + tms[tmp-1]
    for k in link[tmp]:
      fin[k] -= 1
      if fin[k] == 0:
        h.append(k)
  
  ans.append(ans_pool[dest])
for k in ans:
  print(k)

  # h = [i for i in range(1,n+1) if fin[i] == 0]
  # heapq.heapify(h)
  # while h:
  #   tmp = heapq.heappop(h)
  #   ans_pool[tmp] = max([0]+[ans_pool[x] for x in link_rev[tmp]]) + tms[tmp-1]
  #   if tmp == dest:
  #     break
  #   fin[tmp] -= 1
  #   for k in link[tmp]:
  #     fin[k] -= 1
  #     if fin[k] == 0 and not k in h:
  #       heapq.heappush(h,k)
  # ans.append(ans_pool[dest])

  # h = deque([])
  # for i in range(1,n+1):
  #   if fin[i] == 0:
  #     h.append(i)
  #     ans_pool[i] = tms[i-1]
  # while h:
  #   tmp = h.popleft()
  #   for k in link[tmp]:
  #     fin[k] -= 1
  #     ans_pool[k] = max(ans_pool[k], ans_pool[tmp]+tms[k-1])
  #     if fin[k] == 0:
  #       h.append(k)