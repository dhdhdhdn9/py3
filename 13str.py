# 문자열은 문자들의 리스트와 유사
# 따라서, 리스트 슬라이싱을 통해 문자열 내 개별 문자를 추출할 수 있음

# '파이썬은완전재미있어요'라는 문자열에서
# 홀수 위치에 있는 문자를 대신하여 '#'을 출력하는 코드 작성

words = '파이썬은완전재미있어요'

wordsL = len(words)
for i in range(wordsL):
    if (i % 2 != 0):
        print(words[i], end='')
    else:
        print('#', end='')


# 문자열 함수
# 대소문자 반환
str = 'Python is easy. 그래서 programming이 재미있어요.'
str.lower()
str.upper()
str.swapcase()
str.title()

# 문자열 찾기
str = '파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠. ^^'
str.count('공부') # 특정 문자열의 갯수
str.find('공부')  # 특정 문자열을 처음 찾은 위치 (왼쪽 기준)
str.find('공부', 5)  # 특정 인덱스 이후로 특정 문자열을 처음 찾은 위치 (왼쪽 기준)
str.find('공부', str.find('공부')+ 1)
str.find('없다')  # 찾지 못하는 경우: -1 출력
str.rfind('공부')  # 특정 문자열을 처음 찾은 위치 (오른쪽 기준)

str.index('공부')
str.index('공부', 5)
str.rindex('공부')
str.index('없다')    # 찾지 못하는 경우: 오류 발생 -> 따라서 되도록이면 find 사용

str.startswith('파이썬')   # 해당 문자열로 시작하는지 여부 확인
str.startswith('파이썬', 10)   # 특정 인덱스 이후 특정 문자열로 시작하는지 여부 확인
str.startswith('물론', 15)   # 특정 인덱스 이후 특정 문자열로 시작하는지 여부 확인
str.endswith('^^')   # 해당 문자열로 끝나는지 여부 확인


# 문자열 내 공백 다루기
str = '  파  이  썬  '
str.strip() # 공백 제거: string 함수
str.rstrip() # 오른쪽 공백 제거
str.lstrip() # 왼쪽 공백 제거

str = '--파--이--썬--'
str.strip('-') # 지정 문자 제거: 매개 변수에는 제거할 문자를 지정
str.rstrip('-') # 오른쪽 공백 제거
str.lstrip('-') # 왼쪽 공백 제거

str = '<<파 << 이 >> 썬>>'
str.strip('<>') # 지정 문자들 제거: 매개 변수에는 제거할 문자를 지정
str.rstrip('<>')
str.lstrip('<>')

str = '열심히 파이썬 공부중~'
str.replace('파이썬','Python')  # 지정한 문자열을 새로운 문자열로 바꿈


str1 = '  파  이  썬  '
str1.replace(' ','')
str2 = '--파--이--썬--'
str.replace('--','')
str3 = '<<파 << 이 >> 썬>>'
str4 = str3.replace('<','')
str5 = str4.replace('>','')
str5.replace(' ','')


# 문자열 분리 결합
str = '혜교, 98, 65, 77'  # 구분기호로 문자열을 분리하고 리스트로 저장
str.split(',')

str = '혜교|98|65|77'
str.split('|')

str = '혜교\r\n98\r\n65\r\n77'
str.split('\r\n')   # 줄바꿈 기호 기준으로 문자열 분리
str.splitlines()

str = ['혜교','98','65','77']
','.join(str)   # 리스트의 각 항목을 구분기호로 결합

result = ''     # join을 사용하지 않는 경우
for s in str:
    result += s + ','


# 객체를 특정 함수에 일괄적으로 적용하기
# map(적용할 함수명, 대상객체)
str = ['123', '456', '789'] # 문자열을 숫자로 변경하고자 함

nums = []   # map을 사용하지 않는 경우
for s in str:
    nums.append(int(s))

nums = list(map(int, str))


# 문자열 정렬하기

# 특정 문자로 채우기


# 문자열 구성 파악하기
# 입력한 값이 영어/한글이면 '글자', 숫자면 '숫자', 섞여 있으면 '글자+숫자',
# 그외 나머지 문자면 '알 수 없음'이라고 출력하는 프로그램

words = input('문자 입력: ')
result = ''
if words.isalpha():
    result = '글자'
elif words.isdigit():
    result = '숫자'
elif words.isalnum():
    result = '글자+숫자'
else:
    result = '알 수 없음'
print(result)






