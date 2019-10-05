# 날짜를 입력하면 요일을 출력하는 프로그램을 완성하시오.
# 예를들어 "20190830"을 입력하면 "fri"를 출력
# 날짜형식은 YYYYMMDD 8자리의 문자열이고, 
# 요일은 mon, tue, wed, thu, fri, sat, sun 3자리의 문자열이다.

import datetime

def solution(inputday):
    days = ['mon','tue','wed','thu','fri','sat','sun']
    year = int(inputday[0:4])
    month = 0
    day = 0
    if inputday[4]=='0':
        month=int(inputday[5])
    else:
        month=int(inputday[4:6])
    
    if inputday[6]=='0':
        day=int(inputday[7])
    else:
        day=int(inputday[6:])

    return str(days[datetime.date(year,month,day).weekday()])

print(solution('20191003'))