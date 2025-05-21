#번호가 낮을수록 쉽고, a번을 풀어야 b번을 풀수 있다...
# 각 정보를 엮어서 "문제를 풀 순서집"을 만들고,
# 그걸 정렬하면서 가장 낮은값을 빼내면 되는건가?
# 트리를 만들라는거랑 같은데..
# import heapq

# def allgood(n,rev,vis):
#   for k in rev[n]:
#     if not vis[k-1]:
#       return False
#   return True

# n, c = map(int,input().split())

# nonroot = []
# injup = {}
# injup_rev={}
# prcs = [False]*n
# ans = []

# for _ in range(c):
#   s,d = map(int,input().split())
#   nonroot.append(d)
#   if injup.get(s) == None:
#     injup[s] = [d]
#   else:
#     injup[s].append(d)

#   if injup_rev.get(d) == None:
#     injup_rev[d] = [s]
#   else:
#     injup_rev[d].append(s)

# h = list(set([x for x in range(1,n+1)])-set(nonroot))
# heapq.heapify(h)

# while h:
#   tmp = heapq.heappop(h)
#   ans.append(tmp)
#   prcs[tmp-1] = True
#   if injup.get(tmp) != None:
#     for nxt in injup[tmp]:
#       if allgood(nxt,injup_rev,prcs):
#         heapq.heappush(h,nxt)
# print(ans)

import heapq
n,e = map(int,input().split())
link = [[] for _ in range(n+1)]
need = [0]*(n+1)
for _ in range(e):
  s,d = map(int,input().split())
  link[s].append(d)
  need[d] += 1
ans = []
h = [i for i in range(1,n+1) if need[i] == 0]
heapq.heapify(h)
while h:
  tmp = heapq.heappop(h)
  ans.append(str(tmp))
  for k in link[tmp]:
    need[k] -= 1
    if need[k] == 0:
      heapq.heappush(h,k)
print(" ".join(ans))
