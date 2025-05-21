import heapq
T = int(input())
ans = []
for _ in range(T):
  n = int(input())
  stck = []
  stck.append(list(map(int,input().split(" "))))
  stck.append(list(map(int,input().split(" "))))

  dp1 = [0 for _ in range(n)] #i열에서 1행거를 뜯는다는 선택지
  dp2 = [0 for _ in range(n)] #i열에서 2행거를 뜯는다는 선택지

  hm2 = []

  if(n == 1):
    ans.append(max(stck[0][0],stck[1][0]))
    continue
  
  dp1[0] = stck[0][0]
  dp2[0] = stck[1][0]
  
  dp1[1] = max(stck[0][1],dp2[0]+stck[0][1])
  dp2[1] = max(stck[1][1],dp1[0]+stck[1][1])
  if(n == 2):
    ans.append(max(dp1[1],dp2[1]))
    continue

  heapq.heappush(hm2, -dp1[0])
  heapq.heappush(hm2, -dp2[0])
  for i in range(2,n):
    m = -heapq.heappop(hm2)
    dp1[i] = max(m+stck[0][i],dp2[i-1]+stck[0][i])
    dp2[i] = max(m+stck[1][i],dp1[i-1]+stck[1][i])
    heapq.heappush(hm2,-m)
    heapq.heappush(hm2,-dp1[i-1])
    heapq.heappush(hm2,-dp2[i-1])
  ans.append(max(dp1[-1],dp2[-1]))
for a in ans:
  print(a)
