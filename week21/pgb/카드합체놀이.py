from sys import stdin
import heapq
input = stdin.readline

n, h = map(int,input().split())

cards = list(map(int,input().split()))
heapq.heapify(cards)

for _ in range(h):
  f = heapq.heappop(cards)
  s = heapq.heappop(cards)
  new = f+s
  heapq.heappush(cards,new)
  heapq.heappush(cards,new)

print(sum(cards))