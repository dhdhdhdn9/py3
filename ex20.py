
# 사칙연산 프로그램
def calculator():
    x = int(input('정수 입력: '))
    y = int(input('정수 입력: '))
    result = []
    result.append(x+y)
    result.append(x-y)
    result.append(x*y)
    result.append(x/y)
    print(f'사칙연산 결과: {result}')
calculator()



# 할인된 상품 가격표 출력 프로그램
header = '-' * 40
header += '\n--한빛마트 오늘의 할인 가격표 출력 시스템--\n'
header += '-' * 40

def products():
    products = {'쌀': 9_900, '상추': 1_900, '고추': 2_900, '마늘': 8_900,
                '통닭': 5_600, '햄': 6_900, '치즈': 3_900}
    return products

def discount():
    p = products()
    sale = int(input('오늘의 할인율을 입력하세요(%): '))
    dc = (100-sale)/100
    print(header)
    for pd, pr in p.items():
        print(f'{pd:3s}: {pr:,d}원 {sale}% DC -> {pr*dc:,.0f}원')
    print('-' * 40)
discount()