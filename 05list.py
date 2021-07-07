

# 파이썬 리스트
attendList = ['순철','변헌','민우','찬호','민태']
print(attendList)

numbers  = [1,2,3,4,5,6,7,8,9,]
print(numbers)

complex = [1,2.0, 3.1415, 40, '5', "6"]
print (complex)

for data in numbers:    # iterable
    print(data)

for data in complex:    # iterable
    print(data)


name = input('메세지 입력: ')
print(f'입력한 문자열 길이: {len(name)}')

print(len('Hello, python!!'))
print(len(['Hello, python!!']))


# 리스트의 모든 항목 조회
print(complex[0])
print(complex[1])
print(complex[2])
print(complex[3])
print(complex[4])
print(complex[5])
for i in range(6):
    print(complex[i])

for i in range(len(complex)):
    print(complex[i])

for item in complex:
    print(item)


for idx, item in enumerate(complex):
    print(f'{idx}, {item}')

print(complex.index(3.1415))


sports = ['baseball', 'basketball', 'tennis', 'golf', 'soccer']
print(f'sports의 마지막 인덱스값: {len(sports)}')


languages = ['c/c++', 'c#', 'python', 'java']
for idx, item in enumerate(languages):
    if item == 'python':
        print(f'python의 인덱스값: {idx}')


hobby = ['독서', '등산', '요리']
hobby.append('배구')
print(hobby)


numbers = [1,2,3,4,5,7,8,9]
numbers.insert(5, 6)
numbers.insert(9, 10)
print(numbers)



weather = ['The', 'weather', 'very']
weather.insert(2, 'is')
weather.insert(4, 'cold')


import operator as op
# 성적처리 프로그램 - 3명의 학생 데이터 입력 후
# 총점, 편균, 학점 처리 후 결과 출력
names = []
kors = []
engs = []
mats = []
tots = []
avgs = []
grds = []

for i in range(3):
    name = input(' 이름: ')
    names.append(name)
    kor = int(input('국어: '))
    kors.append(kor)
    eng = int(input('영어: '))
    engs.append(eng)
    mat = int(input('수학: '))
    mats.append(mat)


for i in range(3):
    tots.append(kors[i] + engs[i] + mats[i])
    avgs.append(tots[i] / 3)
    grds.append('가')
    if 90 <= avgs[i]:
        grds[i] = '수'
    if 80 <= avgs[i] < 90:
        grds[i] = '우'
    if 70 <= avgs[i] < 80:
        grds[i] = '미'
    if 60 <= avgs[i] < 70:
        grds[i] = '양'


# 리스트 수정
# 리스트[인덱스] = 수정할 값
hobby
hobby[1] = '여행'
hobby


# 리스트 삭제
# pop: 맨 뒤의 항목을 제거
# pop(위치): 해당 위치의 항목을 제거
hobby
hobby.pop()
hobby

sports
sports.pop(2)

# remove: 요소값으로 제거
languages
languages.remove('java')
languages.remove('c/c++')


# 과일리스트에서 야채 찾아 삭제하기
fruits = ['사과', '망고', '당근', '수박', '포고', '참외', '토마토']
fruits.pop(5)
fruits.pop(2)
fruits.remove('토마토')
fruits.remove('당근')


import operator as op

# 합격 여부 판정하기
scores = [55, 35, 40, 70, 65, 30]

cnt = len(scores)
tot = 0
fails = 0
for i in range(cnt):
    tot += int(scores[i])
    avg = tot / cnt
    if scores[i] < 40: fails += 1 # 과락수 증가

print(f'40점 미만 과목수: {fails}')
print(f'평균 점수: {avg:.2f}')
if avg < 60 and fails > 0:
    print(f'아쉽습니다. 불합격하셨습니다.')
else:
    print("축하합니다. 합격하셨습니다!")


# 정렬하기
numbers = [5, 1, 3, 4, 2, 6]
numbers.sort()
numbers

numbers.sort(reverse=True) # 내림차순
numbers


# 모의고사 점수
exam = [90,100,88,85,95,92,70,75,100,92,78,80,75,95,90,100,84]
exam.sort(reverse=True)
exam


# 참석자 명단(한글 정렬)
attd = ['김길동', '박길동', '이길동', '정길동', '홍길동']
attd.sort(reverse=False)
attd
attd.sort(reverse=True)
attd


# 영어 정렬
units = ['scv', 'marine', 'firebat', 'ghost', 'dropship', 'battlecruiser', 'valkyrie', 'medic']
units.sort(reverse=False)
units
units.sort(reverse=True)
units


# 리스트 슬라이싱
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
alphabet.sort(reverse=True)
alphabet
alphabet[2:5]

# a b c d e
# 1 2 3 4 5
# a, b, c, d 추출
alphabet[0:4]
alphabet[:4]
alphabet[:-6]

# 슬라이싱 고급기능
alphabet[::-1]
alphabet[1::-1]
alphabet[3::-1]

# d c b a 추출
alphabet[3::-1]
alphabet[-7::-1]
alphabet[-7:-11:-1]

# g h e d 추출



