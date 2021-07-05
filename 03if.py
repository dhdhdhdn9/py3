import operator as op

# if문
# num = int(input('숫자 입력: '))
# if num > 10:
#     print(f'{num}은 10보다 크다')


# 속도 위반 경고하기
# spd = int(input('현재 속도: '))
# if spd > 50:
#     print('속도 위반!')
#     print('주의 하세요!')
# else:
#     print('정상 속도입니다.')


# 합격/불합격 출력: if ~ else
# score = int(input('성적: '))
# if (score >= 80):
#     print('축하합니다! 합격하셨습니다.')
# else:
#     print('아쉽습니다. 다시 도전해주세요.')

# 실행문이 아직 정해지지 않은 경우 pass 키워드로 대체 가능
# if (score >= 80):
#     pass
# else:
#     pass


# 자동 온도 조절 장치
# mchTemp = float(input('현재 기계 온도: '))
# if mchTemp >= 40:
#     print('팬(Fan) 가동')
# else:
#     print('팬(Fan) 중지')

# 자동 온도 조절 장치
# mchTemp = float(input('현재 기계 온도: '))
# if mchTemp >= 40: print('팬(Fan) 가동')
# else: print('팬(Fan) 중지')

#  입력받은 정수를 3으로 나눠 소수점 첫재자리가 0.5 이상인 경우
# 반올림해서 출력하고, 아니면 그대로 출력
# num = int(input('정수 입력:'))
# divide = num / 3
# if (divide - int(divide) >= 0.5):
#     divide = int(divide) + 1
# else:
#     divide = int(divide)
# print(f'결과 : {divide}')


# 마일리지 가능 여부
# milge = 1233
# if (milge >= 1000):
#     print(f'마일리지 사용 가능')
# else:
#     print(f'마일리지 사용 불가')
# 합격/불합격 출력: if ~ else
# score = int(input('성적: '))
# if (score >= 80):
#     print('축하합니다! 합격하셨습니다.')
# else:
#     print('아쉽습니다. 다시 도전해주세요.')


# 성적처리
# score2 = int(input('점수 입력:'))
# if (90 <= score2):
#     print('수')
# elif (80 <= score2 < 90):
#     print('우')
# elif (70 <= score2 < 80):
#     print('미')
# elif (60 <= score2 < 70):
#     print('양')
# else:
#     print('가')


# 자동 주문 시스템
# country = int(input('Good morning. Nice to meet you.\nWhere are you from?\nPlease select a number.\n1.대한민국 2. USA 3. 中國\n선택: '))
# country = int(input('안녕하세요. 만나서 반갑습니다.\n어디서 오셨나요?\n숫자를 선택해주세요.\n1.대한민국 2. USA 3. 中國\n선택: '))
# if op.eq(country, 1):
#     print('주문하시겠어요?')
# elif op.eq(country, 2):
#     print('Would you like to order?')
# elif op.eq(country, 3):
#     print('您要订购吗？')
# elif op.eq(country, 4):
#     print('Would you like to order?')


# 국가 재난 지원금 수령액 조회
# hsehold = int(input('가족 구성원 수: '))
# if op.eq(hsehold, 1):
#     money = 400_000
# elif op.eq(hsehold, 2):
#     money = 600_000
# elif op.eq(hsehold, 3):
#     money = 800_000
# else:
#     money = 1_000_000
# print(f'{money:,.0f}원 지원')


# BMI 지수 계산하고 그에 따른 다양한 결과 출력
# weight = int(input('체중(㎏): '))
# height = int(input('신장(㎝): '))
# bmi = weight / ((height/100) * (height/100))
# if op.gt(bmi, 30):
#     print('고도 비만')
# elif op.gt(bmi, 25):
#     print('비만')
# elif op.gt(bmi, 23):
#     print('과체중')
# elif op.gt(bmi, 18.5):
#     print('정상체중')
# else:
#     print('저체중')


# 버스 전용차로 단속 프로그램
# dayMsg = '1. 월~금, 2. 토요일, 3. 공휴일\n요일 선택: '
# busMsg = '버스 전용차로 단속 중입니다.\n1. 버스, 2. 승용차\n차종 선택: '
# busDay = int(input(dayMsg))
# if op.eq(busDay, 1):
#     busChk = int(input(busMsg))
#     if op.eq(busChk, 1):
#         msg = '버스입니다.'
#     else:
#         msg = '버스 전용차로 위반!'
# else:
#     msg = '토요일 및 공휴일은 단속하지 않습니다.'
# print(msg)


# 출생연도와 마스크 구매
endBirthyear = int(input('출생 연도 끝자리 입력: '))
age = int(input('만 나이 입력: '))
if op.lt(age, 65):
    if op.eq(endBirthyear, 1 or 6):
        whenBuy = '월요일에 구매가 가능합니다.'
    if op.eq(endBirthyear, 2 or 7):
        whenBuy = '화요일에 구매가 가능합니다.'
    if op.eq(endBirthyear, 3 or 8):
        whenBuy = '수요일에 구매가 가능합니다.'
    if op.eq(endBirthyear, 4 or 9):
        whenBuy = '목요일에 구매가 가능합니다.'
    if op.eq(endBirthyear, 5 or 0):
        whenBuy = '금요일에 구매가 가능합니다.'
else:
    whenBuy = '언제든지 구매 가능합니다.'
print(whenBuy)
