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







