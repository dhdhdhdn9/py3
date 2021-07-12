from EMP import EMP
from EMPService import EMPService
from datetime import datetime

emp = EMP(111, '익명', '김', '010-2345-6789', 'anonymous@email.com', '2021-07-09', 'JOB', 78900, 0, 100, 90)
print(emp)

# empsrv = EMPService()   # 객체 생성
# emp = empsrv.readEMP()  # 메서드 호출
# print(emp)

emp = EMPService.readEMP() # 객체 생성 없이 바로 메서드 호출
print(emp)

# now = datetime(2021, 7,12)
# hire = datetime(2003, 6,17)
# days = now - hire
# print(days) # 근무일수

EMPService.computeDuty(emp)
print(emp)

