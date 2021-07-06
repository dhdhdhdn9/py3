import operator as op


# 시스템 관리자 로그인 기능
userid = input('관리자 아이디를 입력하세요.')
pwd = input('관리자 암호를 입력하세요')
for i in range (5):
    if pwd == 'hanbitac' and userid == 'admin':
        print('로그인 됐습니다.')
        break
    if op.ne(pwd, 'hanbitac'):
        input('암호를 다시 확인하세요.')
else:
    print('로그인 실패! 횟수 초과!')

cnt = 1
while True:
    if cnt > 5:
        print('로그인 실패! 횟수 초과!')
        break
    userid = input('관리자 아이디를 입력하세요.')
    pwd = input('관리자 암호를 입력하세요')
    if pwd == 'hanbitac' and userid == 'admin':
        print('로그인 됐습니다.')
        break
    else:
        input('암호를 다시 확인하세요.')
    cnt +=1


