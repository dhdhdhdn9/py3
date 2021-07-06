
import operator as op

# 반복문

# 1~10 까지 정수 출력
# 1부터 10까지 1씩 증가하면서 진행
for i in range(1,10+1):
    print(i)

# 2~10 까지 짝수 출력
for i in range(2,10,2):
    # print(i)
    print(i, end=' ')

for i in range(1, 10+1):
    if i % 2 == 0: print(i, end= ' ')

# 사용자가 입력한 횟수만큼 "메일발송"문자열 출력
end = int(input('메일 발송 횟수: '))
for i in range (1, end+1):
    print('메일 발송!')


# 1~10 사이의 정수를 출력하되, 정수가 3의 백수이면 '3의 배수!' 출력하기
for i in range (1, 11):
    if op.eq(i % 3, 0):
        print('3의 배수!')
    else:
        print(f'num = {i}')


# 구구단 5단
for i in range (1, 10):
    print(f'5 * {i} = {5*i}')


# 사용자로부터 숫자(1 - 9)를 하나 입력 받아, 구구단을 출력하는 프로그램
oneNum = int(input('숫자 입력(1~9): '))
for i in range(1, 10):  # 1부터 9까지
    print(f'{oneNum} x {i} = {oneNum*i}')


# 1~10까지의 정수 합
i = 0
sum = 0
for i in range (1, 11):
    sum += i
print(sum)



# 1~100까지의 정수 중 3과 7의 공배수와 최소공배수
for i in range (1, 100, 1):
    if op.eq(i%3 or i%7, 0):
        print(f'{i}', end=" ")

min = 100
print('3과 7의 공배수:', end = ' ')
for i in range(100, 1, -1):
    if op.eq(i%3 or i%7, 0):
        if min >= i: min = i
        print(i, end = ' ')
print(f'최소공배수: {min}')



for i in range(-10, 1, 1):
    print(i, end = ' ')


# 1~10까지 출력
for i in range(10):
    print(i+1, end= " ")


for i in range(1, 51, 1):
    if op.eq(i%7, 0):
        print(i, end = ' ')
        
        
# 반복문에 range 대신 문자열 사용
for ch in 'Hello':
    print(ch, end= ',')
print()



# 50보다 작은 7의 배수
for i in range(50):
    if op.eq(i%7, 0):
        print(i, end = ' ')


# 1~10까지 출력
num = 1
while op.lt(num, 10+1):
    print(num, end = ' ')
    num += 10


# 1~30까지의 정수 중 홀수와 짝수를 구분하여 출력하기
num = 1
while op.le(num, 30):
    if op.eq(num % 2, 0):
        print(f'짝수: {num}')
    else:
        print(f'홀수: {num}')
    num += 1


# 구구단 3단 출력하기
num = 1
dan = 19
while op.lt(num, 10):
    print(f'{dan} * {num} = {num*dan}')
    num += 1


# 0~100까지 정수 중 3과 8의 공배수와 최소공배수 출력하기
num = 1
min = 999
while op.le(num, 100):
    if op.eq(num % 3 or num % 8, 0):
        print(f'3과 8의 공배수: {num}')
        if op.gt(min, num):
            min = num
    num = num + 1
print(f'3과 8의 최소공배수: {min}')


# 게임 진행과 종료
flag = True
while flag:
    code = int(input('1: 진행, 2: 종료'))
    if op.eq(code, 1):
        print('게임 진행')
    else:
        flag: False
        print('게임 종료')


# 1부터 50까지 정수 중 3의 배수 더하기
sum = 1
for i in range (1, 50+1):
    if op.eq(i % 3, 0): continue    # 3의 배수인 경우에만 계속 진행(continue)
    sum += i
print(sum)


# 1~100까지 모든 정수 더하기
# 단, 정수의 총합 500을 넘기는 정수가 무엇인지 구함
sum = 0
for i in range (1, 100):
    sum += i
    if op.eq(sum, 500):
        print(i)
        break
print(sum, i)


# 1~10 까지 정수의 총합을 구하고 반복이 끝나는 경우 완료 메시지 출력
sum = 0
for i in range(10): # 0~9
    sum += (i + 1)
else:
    print(f'총합 계산 결과: {sum}')


import operator as op

# 삼각형 넓이 구하기
# 단, 가로 길이는 1부터 2의 배수로 증가
# 세로 길이는 1부터 3의 배수로 증가
# 삼각형 넓이가 150보다 크면 프로그램 종료
width = 2
height = 3
size = 0
while op.le(size, 150):
    size = (width * height)/2
    print(f'삼각형 넓이: {size}')
    width += 2
    height += 3


# 1~100까지 정수 중 5 또는 7의 배수를 제외하여 출력
for i in range (1, 100):
    if op.eq(i % 5 and i % 7, 0): continue
    print(i, end = ' ')
print()


# 구구단 출력
for i in range (1, 10):
    for dan in range (1, 10):
        print(f'{dan:2d} * {i:2d} = {dan*i:2d} \t', end = ' ')
    print()
print()


# *을 이용한 트리 모양
print('      *')
print('     ***')
print('   ******')
print('  ********')
print(' **********')
print('************')


