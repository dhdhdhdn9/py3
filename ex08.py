
import operator as op
from datetime import datetime as dt

# 차량 2부제 프로그램
carNum = int(input('차량 번호: '))
month = dt.today().month
day = dt.today().day
if op.eq(day % 2, 0):
    oddeven = '짝수'
    if op.eq(carNum % 2, 0):
        msg = '가능'
    else:
        msg = '불가능'
else:
    oddeven = '홀수'
    if op.ne(carNum % 2, 0):
        msg = '가능'
    else:
        msg = '불가능'
print(f'{month}월 {day}일은 {oddeven} 차량만 입차 가능합니다.\n{carNum}번인 귀하의 차량은 입차 {msg}합니다.')