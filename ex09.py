
import operator as op
from datetime import datetime

# 생존율 출력 프로그램
cosTime = int(input('최초 장비를 사용하기까지 걸린 시간: '))
if op.le(cosTime, 360):
    if op.ge(cosTime, 300):
        msg = '47%'
    if op.ge(cosTime, 240) and op.lt(cosTime, 300):
        msg = '57%'
    if op.ge(cosTime, 180) and op.lt(cosTime, 240):
        msg = '66%'
    if op.ge(cosTime, 120) and op.lt(cosTime, 180):
        msg = '76%'
    if op.ge(cosTime, 60) and op.lt(cosTime, 120):
        msg = '85%'
    if op.lt(cosTime, 60):
        msg = '86% 이상'
else:
    msg = '25% 미만'
print(f'생존율: {msg}')

