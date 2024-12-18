def solution(sizes):
    w, h = 0, 0
    for size in sizes :
        size.sort()
        w = max(w, size[0])
        h = max(h, size[1])
    
    return w * h