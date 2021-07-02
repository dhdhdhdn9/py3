
num1 = 10
num2 = 20
num3 = num1 + num2 # 정수 + 정수 = 정수

num1 = 30.5
num2 = 50.5
num3 = num1 + num2 # 실수 + 실수 = 실수

num1 = 10
num2 = 30.5
num3 = num1 + num2 # 정수 + 실수 = 실수


# janSal = 30000000
# febSal = 28000000
# marcSal = 29000000
# janSal = int(input('1월 매출: '))
# febSal = int(input('2월 매출: '))
# marcSal = int(input('3월 매출: '))
# frstQurtSal = janSal + febSal + marcSal
# print('1분기 전체 매출: {0}원'.format(frstQurtSal))

# 1분기 수입
# qurtSal = 50000000
# qurtPrch = 34000000
# qurtSal = int(input('1분기 매출: '))
# qurtPrch = int(input('1분기 매입: '))
# revenue = qurtSal - qurtPrch
# print('수익: {0}원'.format(revenue))


# 방 너비 구하기
# horiz = int(input('가로 길이: '))
# vrtic = int(input('세로 길이: '))
# roomArea = horiz * vrtic
# print('방 넓이: {0}㎠'.format(roomArea))

# str1 = 'Hello, world! '
# str1 * 5
# 5 * str1
# 5 * str1 * 7
# str1 * - 1
# str1 * 0.1


# BMI 구하기
# weight = int(input('몸무게(㎏): '))
# height = float(input('신장(m): '))
# bmi = weight / (height*height)
# print('BMI 수치: {0:.2f}'.format(bmi))
# print(f'BMI 수치: {bmi:.2f}')
# :.2f -> 소수점 2번째 자리 까지
# f-string: py 3.6부터 지원

# print 출력 속도: .format > % > f-string


# 동전 갯수 알아보기
# coinNum = int(input('손 안의 동전 수: '))
# oddEven = coinNum % 2
# print(f'{oddEven}')


# 빵 나눠줄 빵 갯수 입력받음
# 최대 몇명가지 나눠줄 수 있는지와 남는 빵 출력
# bread = int(input('빵의 갯수: '))
# diver = int(input('나눠줄 빵의 갯수: '))
#
# stud = bread // diver
# divmod = bread % diver
#
# print(f'{bread}개의 빵은 {diver}개 씩, {stud}명의 학생에게 나눠줄 수 있고, ')
# print(f'{divmod}개의 빵이 남는다.')

2 ** 3
2 ** 7
2 ** 8

infect = 2 ** 29
print(f'30일 후 감염자 수는 {infect}명')


# 복리 계산기
depost = 5000000
intRate = float(depost * 0.05 + depost)
# intRate2 = float(intRate1 * 0.05 + intRate1)
intRate += intRate * 0.05
# intRate3 = float(intRate2 * 0.05 + intRate2)
intRate += intRate * 0.05
# intRate4 = float(intRate3 * 0.05 + intRate3)
intRate += intRate * 0.05
# intRate5 = float(intRate4 * 0.05 + intRate4)
intRate += intRate * 0.05
print(f'{intRate}')




# 범퍼카 탑승가능 여부 확인
height = 120
rideOk = height > 120
print(f'범퍼카 탑승가능여부: {rideOk} (True: 탑승가능, False: 탑승불가능)')

'a' == 'b'
'a' >= 'b' # 아스키 코드로 변환 후 비교


# 범퍼카 탑승가능 여부 확인2
height2 = 150
limit = height2 >= 120
limit2 = height2 < 170
rideOk2 = 120 <= height2 < 170
print(f'범퍼카 탑승가능여부2: {rideOk2} (True: 탑승가능, False: 탑승불가능)')



# short circuit evaluation

num1 = 17
num2 = 20
(num1 < 15) and (num2 > 15) # False and True

num1 = 10
num2 = 20
(num1 < 15) and (num2 < 15) # True and False

# (num1 < 5) and xyz # py38만 지원

# 삼항 연산자
# 참일 때 값 if 조건식 else 거짓일 때 값

num = 11
'짝수' if ( num % 2 == 0) else '홀수'

# 적자/흑자 판단 하기
# 수입: 4000000
# 지출: 3000000
# income = int(input('수입: '))
# outlay = int(input('지출: '))
income = 400000
outlay = 300000
'흑자' if ( income > outlay) else '적자'
# result = '흑자' if ( income > outlay) else '적자'
# print(result)

# 윤년
# 4로 나누어 떨어지고 100으로 나누어 떨어지나, 400으로 나누어 떨어지면 윤년
# year = int(input('년도: '))
year = 1942
isLeap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
'윤년' if (isLeap) else '평년'
# result2 = '윤년' if (isLeap) else '평년'
# print(result2)



