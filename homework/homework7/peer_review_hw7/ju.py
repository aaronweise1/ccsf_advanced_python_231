#!/usr/bin/env python

# I have copied and pasted contents of myCalculation.py file below at the end in """  """ to test. Please copy it in different file and save it with file_name  'myCalculation.py' 


import myCalculation
import unittest
from datetime import date

class TestCalculations(unittest.TestCase):

 def test_yourAge_birthday_sameYear_greaterThan_currentmonth(self):
  result = myCalculation.yourAge("2020-05-19")
  self.assertEqual(result, "Invalid birthdate")

 def test_yourAge_birthday_sameYear_lessThan_currentmonth(self):
  result = myCalculation.yourAge("2020-01-19")
  self.assertEqual(result, "2 months")

 def test_yourAge_birthday_greaterYear_than_currentYear(self):
  result = myCalculation.yourAge("2025-07-21")
  self.assertEqual(result, "Invalid birthdate")

 def test_yourAge_birthday_less_than_current_year_greaterThan_currentMonth(self):
  result = myCalculation.yourAge("1995-09-23")
  self.assertEqual(result, "24 years")

 def test_yourAge_birthday_less_than_current_year_lessThan_currentMonth(self):
  result = myCalculation.yourAge("1995-02-23")
  self.assertEqual(result, "25 years")



if __name__ == '__main__':
 unittest.main()





"""


#!/usr/bin/env python
from datetime import date
from datetime import datetime

def yourAge(birthday):
 date1 = date.today()
 birthday = datetime.strptime(birthday, "%Y-%m-%d")

# If same birthday year is same as current year
 if(date1.year ==  birthday.year):
  if(date1.month == birthday.month):
   if(date1.day >= birthday.day):
    return  str(date1.month - birthday.month) + " months"
   else:
    return  "Invalid birthdate"
  elif(date1.month > birthday.month):
   return  str(date1.month - birthday.month) + " months"
  else:
   return "Invalid birthdate"

#If birthday year is greater than current year
 elif(date1.toordinal() < birthday.toordinal()):
  return "Invalid birthdate"

#if birthday year is less than current year
 elif(date1.toordinal() > birthday.toordinal()):
  if(date1.month == birthday.month):
   if(date1.day >= birthday.day):
    return str(date1.year - birthday.year) + " years"
   else:
    return str(date1.year - birthday.year - 1) + " years"
  elif(date1.month < birthday.month):
   return str(date1.year - birthday.year -1) + " years"
  elif(date1.month > birthday.month):
   return str(date1.year - birthday.year) + " years"




"""
