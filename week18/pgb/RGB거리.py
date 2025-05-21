n = int(input())

rgb = []
for _ in range(n):
  rgb.append(list(map(int,input().split())))

dp = [[0 if i != 0 else rgb[0][j] for j in range(3)] for i in range(n)]
for i in range(1,n):
  dp[i][0] = min(dp[i-1][1],dp[i-1][2])+rgb[i][0]
  dp[i][1] = min(dp[i-1][2],dp[i-1][0])+rgb[i][1]
  dp[i][2] = min(dp[i-1][1],dp[i-1][0])+rgb[i][2]
print(min(dp[-1]))