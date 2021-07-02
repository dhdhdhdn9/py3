# 이름, 국어, 영어, 수학을 입력받아
# 총점, 평균, 학점을 출력하는 프로그램
# name = input('이름: ')
# kor = float(input('국어: '))
# eng = float(input('영어: '))
# mat = float(input('수학: '))
# tot = kor + eng + mat
# avg = tot / 3
# grd = '수' if (avg >= 90) else \
#         '우' if (80 <= avg < 90) else \
#         '미' if (70 <= avg < 80) else \
#         '양' if (60 <= avg < 70) else '가'
# print(f'총점: {tot}, 평균: {avg:.1f}, 학점: {grd}')

# operator 모듈을 이용하면 대량의 데이터 처리 시 속도가 향상됨
import operator as op
op.add(10, 20)
op.sub(10, 20)
op.mul(10, 20)
op.floordiv(10, 3) # 정수 몫: //
op.truediv(10, 3) # 실수 몫: /
op.mod(10, 3)
op.pow(2, 30)

op.eq(10, 20)
op.ne(10, 20)
op.gt(10, 20)
op.lt(10, 20)
op.ge(10, 20)
op.le(10, 20)

# false and true
x = op.eq(10, 10)
y = op.gt(30, 20)
op.and_(x, y)
op.or_(x, y)

# 재난지원금 대상 여부
# income = int(input('월 소득: '))
# nowSprt = int(input('지원금 여부(1: 받고 있다, 2: 받고 있지 않다): '))
# icm = op.le(income, 4000000)
# sprt = op.eq(nowSprt, 2)
# result = '수급 대상자' if op.and_(icm, sprt) else '수급 대상자 아님'
# print(result)
