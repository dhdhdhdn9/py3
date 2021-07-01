# 아이디 비번찾기 프로그램을 작성하세요
print('회원정보를 입력해주세요')
eml = input('이메일을 입력하세요 \n')
name = input('이름을 입력하세요 \n')
uid = input('아이디를 입력하세요 \n')
pwd = input('비밀번호를 입력하세요 \n')
print('--------------------')
print('To.' + eml)
print('▶ 아이디 및 비밀번호 확인')
print(name + ' 고객님 안녕하세요.')
print(name + ' 고객님의 아이디와 비밀번호는 아래와 같습니다.')
print('아이디: ' + uid)
print('비밀번호: ' + pwd)

# print 출력 시 변수와 문자열 사이에 , 사용 : 공백이 하나 더 추가
print('====================')
print('To.', eml)
print('▶ 아이디 및 비밀번호 확인')
print(name, '고객님 안녕하세요.')
print(name, '고객님의 아이디와 비밀번호는 아래와 같습니다.')
print('아이디: ', uid)
print('비밀번호: ', pwd)

# format 함수 사용 : 문자열 템플릿으로 출력(py3의 기능)
print('--------------------')
print('To. {0}'.format(eml))
print('▶ 아이디 및 비밀번호 확인')
print('{0} 고객님 안녕하세요.'.format(name))
print('{0} 고객님의 아이디와 비밀번호는 아래와 같습니다.'.format(name))
print('아이디: {0}'.format(uid))
print('비밀번호: {0}'.format(pwd))

# format 문자열 사용: py2
print('====================')
print('To. %s'%eml)
print('▶ 아이디 및 비밀번호 확인')
print('%s 고객님 안녕하세요.'%name)
print('%s 고객님의 아이디와 비밀번호는 아래와 같습니다.'%name)
print('아이디: %s'%uid)
print('비밀번호: %s'%pwd)




