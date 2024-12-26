'''
예약 손님 다 받을 수 있는 최소 객실 수 리턴
10분 후 이용가능.
==========
구현, 정렬
==========

일단 시작 시간으로 정렬해야 함.
종료 시간에 10분씩 더해야 함.

["16:40", "18:20"]

[(16, 40), (18, 30)]

'''
def preprocess_end_time(hh, mm) :
    hh = int(hh)
    mm = int(mm) + 10
    
    if mm >= 60 :
        hh += 1
        mm -= 60
    
    return hh, mm

def solution(book_time):
    # 1. 시작 시간 순으로 정렬 + 전처리(문자열 -> 숫자)
    book_time.sort(key=lambda x:x[0])
    
    for i in range(len(book_time)) :
        start_time = tuple(map(int, book_time[i][0].split(":")))
        hh, mm = book_time[i][1].split(":")
        end_time = preprocess_end_time(hh, mm)
        book_time[i] = [start_time, end_time]
    
    # 2. 방 개수 구하기
    answer = []
    t = book_time.pop(0)
    answer.append(t)
    
    for bt in book_time :
        flag = False
        for i in range(len(answer)) :
            # 종료시간 vs 시작시간 비교
            if (answer[i][1][0] < bt[0][0]) or \
                (answer[i][1][0] == bt[0][0] and answer[i][1][1] <= bt[0][1]) :
                answer[i] = bt
                flag = True
                break
        if not flag :
            answer.append(bt)
            
    return len(answer)