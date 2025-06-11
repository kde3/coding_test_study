
# n일동안 맥주 n개 (하루에 1개)
# n일동안, k종류의 맥주중에 하나씩 골라 총 n개를 먹을거고(중복 x), n일동안 먹은 술의 선호도의 합이 m을 넘어야함
# 단, k종류의 맥주중 일정 이상의 도수를 가진건 못먹음.

from sys import stdin
input = stdin.readline

n,m,k = map(int,input().split())
beers = []
for _ in range(k):
  sat, al = map(int,input().split())
  beers.append((sat,al))

beers = sorted(beers,key = lambda x: (-x[1],-x[0]))
print(beers)

#nlogn의 이분탐색을 할때마다 nlogn의 정렬을 해야됨 이거 맞나?

right = beers[0][1]
left = beers[-1][1]

while right < left:
  mid = (right+left) // 2
# 이 문제 좀 난감하네...
# 푸는 법이 여러가지일거 같아서
