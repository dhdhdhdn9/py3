
# 파일 다루기


# 입력한 성적데이터를 파일에 저장
fname = 'C:/Java/sungjuk.dat'

name = input('이름: ')
kor = int(input('국어: '))
eng = int(input('영어: '))
mat = int(input('수학: '))

f = open(fname, 'w')    # 지정한 파일을 쓰기 모드로 엶
# data = 'Hello, World!'
data = f'{name} {kor} {eng} {mat}'  # 파일에 기록할 내용을 문자열로 작성

f.write(data)
f.close()


# 기록할 성적데이터를 파일로부터 읽어오기
f = open(fname, 'r')
data = f.read()
print(data)
f.close()


# 일정 관리 메모를 입력하여 텍스트 파일에 저장하기
def saveMemo(memo):
    fname = 'C:/Java/myMemo.txt'
    f = open(fname, 'a')    # append 모드로 파일 초기화
    f.write(memo + "\n")
    f.close()

def memoMain():
    memo = input('메모 입력: ')
    saveMemo(memo)

memoMain()


# py3 방식으로 파일 다루기
# 기존 파일입출력 코드에서 불편한 점:
#   파일 작업 후 반드시 close를 해야함
# with 문을 사용하면 명시적으로 close를 사용하지 않아도 됨
with open(fname, 'a') as f:
    f.write('아무말')


# 파일에서 데이터 읽어오기
fname = 'C:/Java/Employees.csv'
with open(fname) as f:
    data = f.read()     # 모든 데이터를 한번에 다 읽어옴
    print(data)

    data = f.readlines()  # 데이터를 한줄에 읽어옴
    print(data)           # 읽어온 결과는 list 형식

    data = f.readline()   # 데이터 한줄을 읽어옴
    print(data)


# Employees.csv에서 사번, 이름, 입사일, 급여를 출력
with open(fname) as f:
    f.readline()    # 첫줄은 읽기만 하고 처리하지 않음
    while True:
        line = f.readline()
        if not line: break  # 읽을 데이터가 없는 경우 작업 중단
        data = line.split(',')  # 문자열을 ,로 분리한 후 리스트로 저장

        empno = data[0]
        frstn = data[1]
        hdate = data[5]
        sal = int(data[7])

        emp = f'{empno} {frstn} {hdate} {sal:,}'
        print(emp)


# 타이타닉 데이터셋을 이용
# 승객이름name, 성별sex, 나이age, 승선위치embarked, 사망여부survived 등을
# 추출해서 출력
# 단, survived가 0이면 '사망', 1이면 '생존'이라 출력함
# 단, embarked S면 'Southamp', c이면 'Cherbourg', q이면 'Queenstown'이라 출력함
fname = 'C:/Java/titanic3b.csv'
with open(fname) as f:
    f.readline()
    while True:
        row = f.readline()
        if not row: break
        data = row.split(',')
        # name = data[2]
        sex = data[2]
        age = data[5]
        embarked = data[9]
        if embarked == 'S': embarked = 'southAmp'
        elif embarked == 'Q': embarked = 'Queenstown'
        elif embarked == 'C': embarked = 'Cherbourg'
        survived = '사망' if data[1] == '0' else '생존'

        psegr = f'{sex} {age} {embarked} {survived}'
        print(psegr)

