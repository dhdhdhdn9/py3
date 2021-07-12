class EMP:
    def __init__(self, empno, fname, lname, email, hp, hdate, jobid='', salary='', comm='', mgr='', deptid=''):
        self.__empno = empno
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__hp = hp
        self.__hdate = hdate
        self.__jobid = jobid
        self.__salary = salary
        self.__comm = comm
        self.__mgr = mgr
        self.__deptid = deptid

    def __str__(self):
        result = f'{self.__empno} {self.__fname} {self.__lname} {self.__email} {self.__hdate} {self.__hp}' \
                 f'{self.__jobid} {self.__salary} {self.__comm} {self.__mgr} {self.__deptid}'
        return result

    @property
    def empno(self):
        return self.__empno
    @empno.setter
    def empno(self, empno):
        self.__empno = empno

    @property
    def fname(self):
        return self.__fname
    @fname.setter
    def fname(self, fname):
        self.__fname = fname

    @property
    def lname(self):
        return self.__lname
    @lname.setter
    def lname(self, lname):
        self.__lname = lname

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def hdate(self):
        return self.__hdate
    @hdate.setter
    def hdate(self, hdate):
        self.__hdate = hdate

    @property
    def hp(self):
        return self.__hp
    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @property
    def jobid(self):
        return self.__jobid
    @jobid.setter
    def jobid(self, jobid):
        self.__jobid = jobid

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    @property
    def comm(self):
        return self.__comm
    @comm.setter
    def comm(self, comm):
        self.__comm = comm

    @property
    def mgr(self):
        return self.__mgr
    @mgr.setter
    def mgr(self, mgr):
        self.__mgr = mgr

    @property
    def deptid(self):
        return self.__deptid
    @deptid.setter
    def deptid(self, deptid):
        self.__deptid = deptid


