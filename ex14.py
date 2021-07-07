# 출석부 관리 시스템
students = ['정우람', '박으뜸', '배힘찬', '천영웅', '신석기', '배민규', '전민수', '박건우', '박찬호', '이승엽']
# 가나다순 정렬
students.sort(reverse=False)
# 박찬호의 전학
students.remove('박찬호')
students
# 선생님을 돕기 위해 앞의 3명 출력
students[:3]
# 전학생 이병규
students.append('이병규')
students
# 자리바꿈(역순 정렬)
students.sort(reverse=True)
students
# 정우람의 개명 (정잘남)
students[2] = '정잘남'
students