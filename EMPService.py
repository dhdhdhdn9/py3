from EMP import EMP
from datetime import datetime

class EMPService:
    # 객체 생성 없이 바로 사용 가능한 static method로 선언
    @staticmethod
    def readEMP():  # 사원번호, 이름, 성, 이메일, 전화번호, 입사일 등 입력
        empno = input('사원 번호: ')
        fname = input('이름: ')
        lname = input('성: ')
        email = input('이메일: ')
        hp = input('전화 번호: ')
        hdate = input('입사일: ')
        return EMP(empno, fname, lname, email, hp, hdate)

    @staticmethod
    def computeDuty(emp):  # 입사일 기준 근무일 계산
                        # 입력값: 2003 = 06 - 17
        hdate = emp.hdate.split('-')
        now = datetime.now()
        hire = datetime(int(hdate[0]), int(hdate[1]), int(hdate[2]))
        days = now - hire   # 근무일수
        print(str(days).split(' ')[0], '일')  # 6600 days, 12:47:53.715744

