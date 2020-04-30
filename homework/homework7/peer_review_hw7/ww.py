#This is what I think we should do?
import unittest
from datetime import date
from datetime import timedelta
a = date(1000,1,1)
b = date(1000,1,11)
c = timedelta(days = 10)

class Test(unittest.TestCase):
	def testDateAdd(self):
		result = a+c
		self.assertEqual(result,b)

	def testDateSubtraction(self):
		result = b-a
		self.assertEqual(result,c)

if __name__ == '__main__':
	unittest.main()

