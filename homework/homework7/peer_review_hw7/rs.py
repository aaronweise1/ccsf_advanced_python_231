
from datetime import timedelta, datetime, date, time
import unittest

class TimeDeltaTest(unittest.TestCase):
    a = datetime(year=2020, month=1, day=1)
    b = datetime(year=2020, month=1, day=5)

    def addDate(a, b):
        ResultAdd = a +b
        print("Add Date:  ", ResultAdd)
        return ResultAdd

    def subDate(a, b):
        ResultSub = b -a
        print ("Subtract Date:  ", ResultSub)
        return ResultSub

r1 = TimeDeltaTest()
T1 = r1.b - r1.a
T2 = r1.a.day + r1.b.day
T3 = TimeDeltaTest.subDate(r1.b, r1.a)
T4 = TimeDeltaTest.addDate(r1.b.day, r1.a.day)

print ("dateTime subtract:  ", T1)
print ("dateTime subtract:  ", T3)
print ("dateTime Add",  T2)
print ("dateTime Add:  ", T4)


if __name__ == '__main__':
    unittest.main()
