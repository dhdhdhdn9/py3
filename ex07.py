
import operator as op


# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램
# oneNum = int(input('숫자 입력(1~9): '))
# print(f'{oneNum} x 1 = {oneNum*1}')
# print(f'{oneNum} x 1 = {oneNum*2}')
# print(f'{oneNum} x 1 = {oneNum*3}')
# print(f'{oneNum} x 1 = {oneNum*4}')
# print(f'{oneNum} x 1 = {oneNum*5}')
# print(f'{oneNum} x 1 = {oneNum*6}')
# print(f'{oneNum} x 1 = {oneNum*7}')
# print(f'{oneNum} x 1 = {oneNum*8}')
# print(f'{oneNum} x 1 = {oneNum*9}')
# for i in range(1, 10):  # 1부터 9까지
#     print(f'{oneNum} x {i} = {oneNum*i}')



# 키보드로 정수를 하나 입력받아 그 값이 정수, 음수, 0인지 구분하는 프로그램을 작성
# 각각의 경우에 따라 “정수입니다”, “음수입니다”, “0입니다”라고 출력
# oneNum = int(input('숫자 입력: '))
# kindNum = '정수입니다.' if op.ge(oneNum*10, 10) else \
#             '음수입니다.' if op.lt(oneNum, 0) else \
#             '0입니다.'
# print(kindNum)



# 지금 현재 수지의 통장잔액이 25,000원
# 은행이자가 연 6%라 가정할 때, 몇 년이 지나야 통장잔액이 지금의 2배를 넘는지
# 알아보는 프로그램
left = 25000
yIntrt = 0.06
period = int(input('몇년 후: '))
double = left * ((1 + yIntrt) ** period)
inBank = op.gt(double, 50000)
nowMon = '2배를 넘었습니다.' if op.eq(inBank, True) else '2배를 넘지 못했습니다.'
print(f'{period}년 후 {nowMon}')
