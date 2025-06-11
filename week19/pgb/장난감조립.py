from sys import stdin
from collections import deque
input = stdin.readline

# n -> 완제품 / 1~n-1은 소부품
# m개의 줄에 있는 a,b,c
# 부품 a를 만드는데 b가 c개 필요하다

# 그러면 거꾸로 거슬러올라가야겠네

n = int(input())
m = int(input())

link_rev = [[] for _ in range(n+1)]
degree_rev = [0 for _ in range(n+1)] 

for _ in range(m):
  prdt,mtr,k = map(int,input().split())
  link_rev[prdt].append((mtr,k))
  degree_rev[mtr] += 1

# 1~n-1까지가 부속부품이고, n번이 완본체

parts = [0]*n #(1번부터 n-1번 만큼의 부품 개수)
parts.append(1) #(n번=완본체가 1개)
basic = [i for i in range(1,n+1) if not link_rev[i]]

q = deque([n])
while(q):
  tmp = q.popleft()
  if link_rev[tmp]:
    for mtr,k in link_rev[tmp]:
      parts[mtr] += (parts[tmp]*k)
      degree_rev[mtr] -= 1
      if degree_rev[mtr] == 0:
        q.append(mtr)
    parts[tmp] = 0

for i in basic:
  print(i,parts[i])
