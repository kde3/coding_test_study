from sys import stdin
input = stdin.readline

n = int(input())
rep = []
for _ in range(n):
  rep.append(int(input()))

rep = sorted(rep)
cnt = 1
ans = 0
for i in range(n):
  if rep[i] < cnt:
    continue
  if rep[i] > cnt:
    ans += (rep[i]-cnt)
    rep[i] = cnt
  cnt += 1
print(ans)

# 1) 모두 1씩 감소
# 2) 1명이라도 0이 됐다면 1)로 돌아감, 안됐다면 종료

# 프로그램 실행 전에 사전작업으로 1씩 줄일거임. 1명당 1일때 몇명?

# 가장 현실적으로는 연쇄적으로 없애야 하니까,
# 1,2,3,~~~,n 이렇게 만들어야 됨.
# 정렬해서 기준점씩 빼기


# 안되는 케이스들이 있어서 실패한거
# 이거 그냥 산수인데?
# n명이면 1~n을 만들어야 하니 n(n+1)/2고, 그럼 그만큼을 만들면 되잖아.

# n = int(input())
# rep_s = 0
# rep = set([])
# for _ in range(n):
#   tmp = int(input())
#   if tmp in rep:
#     n -= 1
#   else:
#     rep.add(tmp)
#     rep_s += tmp

# print(rep_s - (n*(n+1)//2))