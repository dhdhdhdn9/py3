# 계산기 프로그램
def calculator():
    num1 = int(input('첫번째 숫자 입력: '))
    math = int(input('연산자 입력(1.덧셈, 2.뺄셈, 3.곱셈, 4.나눗셈): '))
    num2 = int(input('두번째 숫자 입력: '))
    compute(num1, math, num2)

def compute(num1, math, num2):
    if math == 1:
        num = num1 + num2
        print(f'덧셈 결과: {num}')
    elif math == 2:
        num = num1 - num2
        print(f'뺄셈 결과: {num}')
    elif math == 3:
        num = num1 * num2
        print(f'곱셈 결과: {num}')
    elif math == 4:
        num = num1 / num2
        print(f'나눗셈 결과: {num}')
    else:
        print('연산자를 잘못 입력하셨습니다.')

calculator()