# 로그인

members = {}
flag = True

menu = '-' * 30
menu += '\n    회원가입 프로그램     \n'
menu += '-' * 30
menu += '\n 1. 회원가입       \n'
menu += ' 2. 프로그램 종료       \n'
menu += '-' * 30

while flag:
    print(menu)
    choice = input('작업을 선택하세요: ')
    if choice == '1':
        userid = input('아이디: ')
        passwd = input('비밀번호: ')
        members[userid] = passwd
    elif choice == '2':
        print('가입한 회원들을 소개합니다.')
        for u, p in members.items():
            print(f'{u}: {p}')
        print('프로그램을 종료합니다.')
        flag = False # 시스템 종료

#
# userid = []
# passwd = []
# regi = {}
#
# print('-'*20)
# choice = int(input('1. 회원가입\n2. 프로그램 종료'))
# print('-'*20)
# if choice == 1:
#     print('회원가입')
#     userid = input('아이디: ')
#     passwd = input('비밀번호: ')
#     regi[userid] = passwd
#     print('-' * 20)
#     choice = int(input('1. 회원가입\n2. 프로그램 종료'))
#     print('-' * 20)
# if choice == 2:
#     print('-'*20)
#     print('아이디 : 비밀번호')
#     print('-'*20)
#     regi = {key: val for key, val in zip(userid, passwd)}
#     for k, v in regi.items():
#         print(f'{k}: {v}')
#     print('-'*20)