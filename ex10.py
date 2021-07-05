
import operator as op
from datetime import datetime


# 전기 요금 계산기
electUse = float(input('전기 사용량: '))
if op.le(electUse, 400):
    if op.gt(electUse, 200):
        rate = 1600
        price = 187.9
    if op.le(electUse, 200):
        rate = 910
        price = 99.3
else:
    rate = 7300
    price = 280.6
electPay = electUse * price + rate
print(f'사용량: {electUse:.1f}kwh\n기본요금: {rate:,}원\n단가: {price}원\n전기 요금: {electPay:,.1f}원')












