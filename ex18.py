# 다국어 인사말 프로그램
def lang():
    print('당신의 국적은?\nWhere are you from?')
    c = int(input('1.한국, 2.USA, 3.Japan, 4.China'))
    if c == 1:
        print('안녕하세요.')
    elif c == 2:
        print('Hello.')
    elif c == 3:
        print('こんにちは。')
    elif c == 4:
        print('你好。')
lang()

