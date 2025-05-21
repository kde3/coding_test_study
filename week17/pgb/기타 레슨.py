n,m = map(int,input().split(" "))
time = list(map(int,input().split(" ")))
left = 1
right = sum(time)

if m == 1:
  print(right)
else:
  while(left < right):
    cnt = 0
    mid = (left+right) // 2
    tmp = 0
    ind = 0
    while(ind < n):
      if cnt == m:
        break
      if tmp + time[ind] <= mid:
        tmp += time[ind]
        ind += 1
      else:
        tmp = 0
        cnt += 1
    if cnt == m:
      left = mid + 1
    else:
      right = mid
  print(right)
  # fin = []
  # ind = 0
  # while(ind < n):
  #     print(ind,tmp)
  #     if tmp + time[ind] <= left:
  #       tmp += time[ind]
  #       ind += 1
  #     else:
  #       fin.append(tmp)
  #       tmp = 0
  # fin.append(tmp)
  # print(fin)
