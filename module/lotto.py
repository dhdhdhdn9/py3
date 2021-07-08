# 로또

import random as r

# def makeLotto():
#     makeNums = []
#     for i in range(6):
#         randNum = r.randint(1, 45)
#         makeNums.append(randNum)
#     return makeNums
#
# def readLotto():
#     readNums = []
#     print('1개부터 45까지의 정수 6개를 입력하시오.')
#     for i in range(6):
#         num = int(input(f'Number {i + 1}: '))
#         readNums.append(num)
#     return readNums

def makeLotto():
    makeNums = []
    while len(makeNums) <6:
        randNum = r.randint(1, 45)
        if makeNums.count(randNum) == 0:
            makeNums.append(randNum)
    return makeNums


def readLotto():
    readNums = []
    i = 1
    print('1개부터 45까지의 정수 6개를 입력하시오.')
    while len(readNums) < 6:
        num = int(input(f'Number {i}: '))
        if readNums.count(num) == 0:
            readNums.append(num)
            i += 1
    return readNums


def makeRandom():
    myNums = readLotto()
    nums = makeLotto()
    chk = []

    for v in myNums:
        if nums.count(v) != 0: chk.append(v)

    print(f'이번주 로또 번호: {nums}')
    print(f'내가 선택한 로또 번호: {myNums}')
    print(f'일치하는 숫자: {chk}')


a = [1,2,3]
b = [1,2,4]
b.count(a[0])


# num1 = int(input('Number 1: '))
# myNums.append(num1)
# num2 = int(input('Number 2: '))
# myNums.append(num2)
# num3 = int(input('Number 3: '))
# myNums.append(num3)
# num4 = int(input('Number 4: '))
# myNums.append(num4)
# num5 = int(input('Number 5: '))
# myNums.append(num5)
# num6 = int(input('Number 6: '))
# myNums.append(num6)