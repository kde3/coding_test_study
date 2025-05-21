# n개의 구간, 제한시간 k 
# 구간마다 도보-도보모금-자전거-자전거모금으로 값 4개
# 제한 시간 이내중에 최대금액

# 2차원 dp -> 몇개째의 구간, 현재 시간에서의 최대값

# n, k = map(int,input().split())
# rt = [list(map(int,input().split())) for i in range(n)]

# dptable = [{0:0}]

# def renew(mp,a,b):
#   if mp.get(a) == None:
#       mp[a] = b
#   else:
#       mp[a] = max(mp[a],b)
#   return mp

# for i in range(n):
#   nxt = {}
#   tmp = [(t,v) for t,v in list(dptable[i].items())]
#   for st,mny in tmp:
#     wnt = st+rt[i][0]
#     wnm = mny+rt[i][1]
#     if wnt <= k:
#       nxt = renew(nxt,wnt,wnm)
    
#     bnt = st+rt[i][2]
#     bnm = mny+rt[i][3]
#     if bnt <= k:
#       nxt = renew(nxt,bnt,bnm)
#   dptable.append(nxt)

# print(max(dptable[-1].values()))


def solution(n, k, A) :
  dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
  base = 0
  limit = 0
  for (i, [t1, m1, t2, m2]) in enumerate(A) :
      if i == 0:
          dp[i+1][t1] = m1
          dp[i+1][t2] = m2
      else:
        for j in range(base,min(limit+1,k+1)):
          if dp[i][j] != 0:
            if j+t1 <= k:
              dp[i+1][j+t1] = max(dp[i+1][j+t1], dp[i][j] + m1)
            if j+t2 <= k:
              dp[i+1][j+t2] = max(dp[i+1][j+t2], dp[i][j] + m2)
      base += t2
      limit += t1
  return max(dp[-1])

n, k = map(int, input().split())
A = []
for _ in range(n) :
    A.append(list(map(int, input().split())))
print(solution(n, k, A))