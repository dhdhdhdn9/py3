# 패키지 package
# 함수, 클래스들을 용도별로 분리해서
# 작성하는 것을 모듈이라 했음

# 그런데, 이러한 모듈들이 모여 뒤죽박죽 섞여 있으면
# 이해도, 활용도가 떨어질수 있음

# 따라서, 모듈들 역시 성격에 맞게 분류해서 관리해야 할 필요성이 대두
# - 패키지를 이용해서 모듈들을 관리

# 파이썬에서는 패키지를 만들려면
# 디렉토리 생성 -> __init__.py 파일 생성하면 됨 (py2)
# python3 이상 __init__.py 를 만들지 않아도
# 패키지로 인식
# => python2와의 호환을 위해 생성할 것을 권장

# 모듈 불러오기
# import 패키지명.모듈파일명
# 모듈명 줄여쓰기: as

import module.calculator as cal

# 정의한 모듈의 특정 기능을 사용하려면
# '패키지명.모듈명.함수명'으로 호출
cal.add(8, 2)
cal.mul(8, 2)
cal.div(8, 2)
cal.sub(8, 2)


# 단위 변환 프로그램
import module.ConvertUnit as cvu

data = int(input('변환할 길이(mm): '))
result = cvu.convertLength(data)
cvu.printUnits(result)



# 시험 여부 통과
import module.ExamUnit as exu

one = int(input('1과목 점수: '))
two = int(input('2과목 점수: '))
three = int(input('3과목 점수: '))
score = exu.calScore(one, two, three)
exu.printScores(score)



# 모듈 중에서 특정 함수만 사용하고 싶을 때는
# 'from 패키지명.모듈명 import 함수명' 형식을 사용

from module.calculator import add
from module.calculator import div # 가독성을 위해 추천

from module.calculator import add, div



# 수학 모듈
import math as m
print(m.ceil(10.5)) # 반올림
print(m.ceil(10.1))
print(m.floor(10.1)) # 내림

import random as r
print(r.random())
print(r.randint(1, 45)) # 1-45
print(r.randrange(1, 45)) # 1-44
print(r.sample(range(1,10),3)) # 표본추출
print(r.choice(range(1,10)))


# 점심메뉴 추천 프로그램
lunches = ['감자튀김이 포함된 햄버거 세트', '김치볶음밥', '돈까스', '피자', '샐러드', '서브웨이']
idx = r.sample(range(6), 1)[0]
idx = r.randint(0, 5)
idx = r.randrange(0, 6)
idx = r.choice(range(6))
print(f'오늘의 점심:',r.choice(lunches))
print(f'오늘의 점심: {lunches[idx]}')



import time as t
print(t.time())
print(t.localtime()) #요일(wday)은 월요일을 기준으로 0 ~ 7

fmt = '%Y-%m-%d %H:%M:%S'
print(t.strftime(fmt, t.localtime()))

print('카운트 다운을 시작합니다.')
t.sleep(1) # 1초 동안 실행 대기
print(5)
t.sleep(1)
print(4)
t.sleep(1)
print(3)
t.sleep(1)
print(2)
t.sleep(1)
print(1)
t.sleep(1)
print('끝!')



# 할인율 적용 프로그램
from module.sale import discountGoods
discountGoods()


# 로또 당첨 프로그램
from module.lotto import makeRandom
makeRandom()
