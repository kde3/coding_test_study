n = int(input())
gls = []
for _ in range(n):
  gls.append(int(input()))

dp = [[0,gls[0],gls[0]]]

for i in range(1,n):
  tmp = dp[i-1]
  ps = max(tmp[0],tmp[1],tmp[2])
  fir = tmp[0] + gls[i]
  sec = tmp[1] + gls[i]
  dp.append([ps,fir,sec])

print(max(dp[-1]))