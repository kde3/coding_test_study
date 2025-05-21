# 문제를 처음 보고 -> 이거 조합인가? 생각을 먼저 했음
# N<=20 c(20,10) -> 이거 가능한..가?

# 검색 -> 죄다 백트래킹
# 풀이를 봤는데, 이건 백트래킹이 아니라 그냥 dfs
# 끝단에 가기 전까지 되돌아 가는 로직이 없어요 풀이에

# 조합 풀이법을 안보고 조합으로 푼거예요

from itertools import combinations

#----- 입력값 받기------
n = int(input())

chrt = []
for i in range(n):
  tmp = list(map(int,input().split()))
  chrt.append(tmp)


#------- 팀 나누기 ---------
pool = [i for i in range(n)]
cmb = combinations(pool,(n//2))

ans = 100000
for c in cmb:
#A,B 팀 나누기
  vis = [True if i in c else False for i in range(n)]
  Ta = [i for i in range(n) if vis[i]]
  Tb = [i for i in range(n) if not vis[i]]
  A = 0
  B = 0

#팀당 2명 이상인 경우, a,b,c -> (a,b) (b,c) (a,c)
#팀 내에서 가능한 조합 뽑기
  As = combinations(Ta,2)
  Bs = combinations(Tb,2)
  for t in As:
    A += (chrt[t[0]][t[1]] + chrt[t[1]][t[0]])
  for t in Bs:
    B += (chrt[t[0]][t[1]] + chrt[t[1]][t[0]])
  ans = min(ans,abs(B-A))
print(ans)
