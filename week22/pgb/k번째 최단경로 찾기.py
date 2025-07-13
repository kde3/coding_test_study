import sys
input = sys.stdin.readline
import heapq

n,m,k = map(int,input().split())
injup = [[] for _ in range(n+1)]
for _ in range(m):
  s,e,l = map(int,input().split())
  injup[s].append((e,l))

inf = 2*(10**9)
dijk = [[inf for _ in range(k)] for _ in range(n+1)] # [[0,0,0],[0,0,1],[],[],[],[],[]]
dijk[1][0] = 0

pq = []
heapq.heappush(pq, (0, 1))

while pq:
   dist, cur = heapq.heappop(pq)
   for nxt,l in injup[cur]:
      ndist = dist+l
      if ndist < dijk[nxt][-1]:
        dijk[nxt][-1] = ndist
        dijk[nxt].sort()
        heapq.heappush(pq,(ndist,nxt))

#print(dijk)

# 결과 출력 예시
for dists in dijk[1:]:
  if dists[k-1] == inf:
    print(-1)
  else:
    print(dists[k-1])


# 거리 자체에도 heap을 쓰는 방법이 있긴 한듯
# import sys
# input = sys.stdin.readline
# import heapq


# n,m,k = map(int,input().split())
# injup = [[] for _ in range(n+1)]
# for _ in range(m):
#   s,e,l = map(int,input().split())
#   injup[s].append((e,l))

# dijk = [[] for _ in range(n+1)]
# heapq.heappush(dijk[1],0)

# pq = []
# heapq.heappush(pq, (0, 1))

# while pq:
#    dist, cur = heapq.heappop(pq)
#    for nxt,l in injup[cur]:
#       ndist = dist+l
#       heapq.heappush(dijk[nxt],ndist)
#       if len(dijk[nxt]) <= k:
#         heapq.heappush(pq,(ndist,nxt))

# # 결과 출력 예시
# for dists in dijk[1:]:
#   if len(dists) < k:
#     print(-1)
#   else:
#     print(sorted(dists)[k-1])