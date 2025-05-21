
# def solution(n):
#   if n == 1:
#     return 1
#   elif n == 2:
#     return 2
#   elif n == 3:
#     return 4
#   else:
#     dp = [0]*(n+1)
#     dp[1] = 1
#     dp[2] = 1
#     dp[3] = 1

#     for i in range(1,n):
#       dp[i+1] += dp[i]
#       if i < n-1:
#         dp[i+2] += dp[i]
#       if i < n-2:
#         dp[i+3] += dp[i]
#     return(dp[n]%1000)
from collections import deque
def solution(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    dp = deque([])
    dp.append(1)
    dp.append(2)
    dp.append(4)
    s = sum(dp)
    for _ in range(n-3):
      dp.append(s)
      s = s*2 - dp.popleft() 
    return (dp.pop() % 1000)

n = int(input())
print(solution(n))