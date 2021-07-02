
# 업무 컴퓨터 수량 파악
work = int(input('근무 시간: '))
comp = int(26 // work)
# addcomp = 1 if ( 26 % work) > 0 else 0
print(f'필요한 컴퓨터: {comp}')


# 차량 2부제 프로그램
# carNum = int(input('차량 번호: '))
# day = int(input('오늘 날짜: '))
# even = op.eq(day % 2, 0)
# odd = op.ne(day % 2, 0)
# numEven = op.eq(carNum % 2, 0)
# numOdd = op.ne(carNum % 2, 0)
# result = '귀하의 차량은 입차 가능합니다.' if op.eq(numEven, even) else \
#             '귀하의 차량은 입차 가능합니다.' if op.eq(numOdd, odd) else \
#             '귀하의 차량은 입차 불가능합니다.' if op.ne(numEven, odd) else \
#             '귀하의 차량은 입차 불가능합니다.'
# print(result)

# 생존율 출력 프로그램



# 전기 요금 계산기
# electUse = int(input('전기 사용량: '))
# baseRt = 910
# uPrice = 99.3
# electPay = electUse * uPrice + baseRt
# print(f'전기 요금: {electPay}')


# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램
# oneNum = int(input('숫자 입력(1~9): '))
# gugu1 = 1 * oneNum
# gugu2 = 2 * oneNum
# gugu3 = 3 * oneNum
# gugu4 = 4 * oneNum
# gugu5 = 5 * oneNum
# print(gugu1, gugu2, gugu3, gugu4, gugu5)



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
# left = 25000
# period = int(input('몇년 후: '))
# double = left * ((1 + 0.06) ** period)
# inBank = op.gt(double, 50000)
# nowMon = '2배를 넘었습니다.' if op.eq(inBank, True) else '2배를 넘지 못했습니다.'
# print(nowMon)