import operator as op

# 369 게임

clap = ''
for i in range (1, 100):
    if op.eq(i % 3 and i % 6 or i % 3 and i % 9 or i % 6 and i % 9, 0):
        clap = '짝'
    print(f'{i} {clap}')


clap = ''
for i in range (1, 100):
    if op.eq(i % 3 and i % 6 or i % 3 and i % 9 or i % 6 and i % 9, 0):
        clap = '짝'
    print(f'{i} {clap}')


for i in range(1,100):
    clap = ''
    if op.lt(i, 10):    # 숫자가 한자리라면
        if op.eq(i%3,0):
            clap = '짝'
    else:               # 숫자가 두자리라면
        num1 = i // 10  # 첫째 숫자 추출
        num2 = i % 10   # 나머지 숫자 추출
        if op.eq(num1 % 3, 0):  # 첫째 숫자가 3의 배수라면
            clap += '짝'
        if op.eq(num2%3, 0) and op.ne(num2, 0): # 둘째 숫자가 3의 배수이고 0이 아니라면
            clap += '짝'
    print(f'{i} {clap}', end=' ')
print()

# 미국판 369
# https://www.wikihow.com/Play-Buzz