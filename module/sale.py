
# 할인율 프로그램

def checkDiscount(goods):
    print('구매 목록')
    cnt = len(goods)
    rate = 0.4
    sum = 0
    if cnt == 1:
        rate = 0.05
    elif cnt == 2:
        rate = 0.1
    elif cnt == 3:
        rate = 0.2

    for i in range(cnt):
        sum += goods[i]

    fare = sum - (sum * rate)
    print(f'할인율: {rate}')
    print(f'총 구매금액: {sum}')
    print(f'할인 적용금액: {fare}')

def discountGoods():
    goods = []
    flag = True

    menu = '-' * 30
    menu += '\n    상품구매 프로그램     \n'
    menu += '-' * 30
    menu += '\n 1. 구매       \n'
    menu += ' 2. 종료       \n'
    menu += '-' * 30

    while flag:
        print(menu)
        prd = 0
        choice = input('작업을 선택하세요: ')
        if choice == '1':
            price = int(input('상품의 금액: '))
            goods.append(price)
        elif choice == '2':
            checkDiscount(goods)
            print('프로그램을 종료합니다.')
            flag = False # 시스템 종료
        else:
            print('잘못 선입력하셨습니다.')








# def sale(x):
#     prices = {}
#     prices['가격'] = x
#     cnt = len(prices)
#     if cnt == 1:
#         prices['할인율'] = '5%'
#         prices['가격'] = x * 0.95
#     elif cnt == 2:
#         prices['할인율'] = '10%'
#         prices['가격'] = x * 0.90
#     elif cnt == 3:
#         prices['할인율'] = '20%'
#         prices['가격'] = x * 0.80
#     else:
#         prices['할인율'] = '30%'
#         prices['가격'] = x * 0.70
#     return prices
#
# def printSale(prices):
#     for k, v in prices.items():
#         print(f'{k}: {v}')