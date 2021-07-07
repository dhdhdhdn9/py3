# 딕셔너리
ages = {'박찬호': 48, '박지성':40, '박세리':50, '이승엽': 43}
type(ages)

person = {'이름': '홍길동', '나이': 25, '주소':'서울 종로구 삼일대로', '취미':['운동','독서','영화감상'], '몸무게':88.8}


# 홍길동의 나이와 취미 조회
person['나이']
person['취미']

# 홍길동의 혈액형 추가
# dict에 새로운 항복을 추가할 때는
# 새로운 키와 값으로 구성해야 함
person['혈액형'] = 'A'
person

# dict에 기존 키와 값으로 구성한 항목을 추가하려고 하면
# 기존키에 저장된 값이 변경됨
person['혈액형'] = 'O'

# dict에서 항목 삭제: pop(키)
person.pop('몸무게')

# person.pop('나이')
# person.pop('취미')

delist = ['나이', '취미']
for key in delist:
    person.pop(key)

# dict 모든 항목 출력
person = {'이름': '홍길동', '나이': 25, '주소':'서울 종로구 삼일대로 123', '취미':['운동','독서','영화감상'], '몸무게':88.8}
for key in person.keys():
    print(person[key])


# dict의 키와 값 모두 가져오기: items
person.items()
# 한꺼번에 가져오기
for k, v in person.items():
    print(k, v)


# 중간고사 성적 관리 프로그램
sungjuk = {'C/C++':'A', 'Java':'B+', '네트워킹':'C', '보안':'A',
           '해킹':'F', '시스템':'C+'}
# Java와 시스템 과목의 성적 조회
sungjuk['Java']
sungjuk['시스템']
sungjuk
# 파이썬(A), OS(A+) 성적 추가
sungjuk['파이썬'] = 'A'
sungjuk['OS'] = 'A+'
sungjuk
# Java를 F, 시스템을 A로 수정
sungjuk['Java'] = 'F'
sungjuk['시스템'] = 'A'
sungjuk
# 전체 과목과 성적 조회
for k, v in sungjuk.items():
    print('과목과 성적')
    print(f'{k}: {v}')


# 딕셔너리 for 축약문
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }

# 이름과 성적 리스트를 dict 객체로 재생성
name = ['혜교', '지현', '수지'] # 키
grd = ['수', '양', '미'] # 값
sj = {}

# 반복문 사용x
sj[name[0]] = grd[0]
sj[name[1]] = grd[1]
sj[name[2]] = grd[2]

# 반복문 사용 -> 코드 줄임
for i in range(len(name)):
    sj[name[i]] = grd[i]


# dict comprehension
# { 키/값 표현식 for 키,값 in zip(반복가능객체1, 반복가능객체2) }
sj2 = {key:val for key, val in zip(name, grd)}

# zip: 여러개의 데이터를 하나로 합쳐서
# iterable한 객체로 생성해줌 - 개별 객체는 튜플로 반환
for pair in zip(name, grd):
    print(pair)