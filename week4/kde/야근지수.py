from heapq import heappop, heappush


def solution(n, works):
    heap = []
    for w in works:
        heappush(heap, -w)

    for _ in range(n):
        if not heap:
            break
        h = heappop(heap)
        h += 1

        if h != 0:
            heappush(heap, h)

    return sum(list(map(lambda x: x ** 2, heap)))