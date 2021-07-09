# 함수와 모듈
# 함수는 일정한 작업을 수행하는 코드집합체
# 보통 반복적으로 사용되는 코드들을 함수로 정의해서 사용

# 즉, 반복적으로 사용할 가치가 있는 코드를 한 뭉치로 묶고
# 어떤 입력값을 주면 결과가 반환되도록 사용

# 또한, 여러 코드들을 함수화하면 프로그램의 흐름을
# 일목요연하게 파악하기 쉬움

# 다른 사람과의 협업시 코드가 섞이지 않게
# 하기 위한 목적도 있음 - 모듈



def startSensor():
    print('온도 센서 작동을 시작합니다.')

def stopSensor():
    print('온도 센서 작동을 중지합니다.')

startSensor()
stopSensor()



# 노트북은 몇인치?
def labtop():
    cm = int(input('노트북 길이(㎝): '))
    inch = cm*0.393701
    print(f'노트북 길이: {inch:.2f}inch')
labtop()



# 이동거리
def distance():
    spd = int(input('이동 시간: '))
    hour = int(input('이동 속도: '))
    dPerHr = print(f'이동 거리: {spd*hour}㎞')
    return dPerHr
distance()



# 전역 global 변수와 지역 local 변수
num = 10    # 10
print(f'전역변수 num: {num}')

def local():
    num = 20    # 20
    print(f'함수 내 num: {num}')

local()

print(f'전역변수 num: {num}')   # 10


# 함수 내에서 전역변수 사용하기: global
num = 10    # 10
print(f'전역변수 num: {num}')

def local():
    global num  # 함수 내에서 전역변수를 수정할 수 있도록 함
    num = 20    # 20
    print(f'함수 내 num: {num}')

print(f'전역변수 num: {num}')   # 10(x) -> 20(o)




# 웹사이트 누적 방문 횟수 프로그램
visit = 0

def count():
    global visit    # global visit = 0  # 전역 변수는 초기화 불가
    visit += 1

def menu():
    flag = True
    while flag:
        choice = int(input('1. 웹사이트 방문, 2. 종료 '))
        if choice == 1:
            count()
            print(f'누적방문: {visit}')
        else:
            print(f'전체 방문횟수: {visit}')
            flag = False

menu()  # 함수 호출



x = 10
y = 10
def add():
    print(x + y)
def add(x, y):
    print(x + y)
add()
add(10, 10)



# 함수의 매개변수 갯수를 동적으로 정의하는 방법:
# 매개변수명 앞에 *를 정의해서 함수를 만든다.
# ex. 기존 add 함수는 2개의 매개변수만 받았다.
#     2개보다 많은 매개 변수를 받아 결과를 출력하고 싶다면?
def add(x,y,z):
    print(x+y+z)

def add2(*num):
    sum = 0
    for v in num:
        sum += v
    print(sum)

add2(10,10)
add2(10,10,10,10)
add2(10,10,10,10,10,10,10,10,10,10)



# mms/sms 전송
def computeMs(msg):
    msgSize = len(msg)
    print(f'문자 길이: {msgSize}')
    if msgSize <= 100:
        print('단문메세지 요금 50원이 부과됩니다.')
    elif msgSize >100:
        print('장문메세지 요금 100원이 부과됩니다.')

msg = input('문자 입력: ')
computeMs(msg)



# 함수 정의 시 매개변수를 선언했지만
# 함수 호출 시 인수를 순서대로 입력하지 않을 경우
# -> 인수값 앞에 매개변수 명을 지정

def computeSungJuk(name, kor, eng, mat):
    tot = kor + eng + mat
    avg = tot/3
    print(tot, avg)

computeSungJuk('혜교', 98,78,65)

computeSungJuk(98,78,65,'혜교') # 오류 발생!
computeSungJuk(98,78,65,name='혜교') # 오류 발생!

computeSungJuk(kor=98,eng=78,mat=65,name='혜교')
computeSungJuk(name='98',eng=78,mat=65,kor='혜교')



# 매개변수를 정의했지만
# 매개변수 없이 함수 호출하고 싶다면?
# -> 매개변수 선언시 초기값을 지정함

def add3(x = 100, y=10):
    print(x + y)

add3(10, 10)
add3()




