#HW: Use UNITTEST to test program with time object calculations 

import VKHWTestTimedeltav2
import unittest

class TestAdd(unittest.TestCase):
    def test_time_gap(self):
        result = VKHWTestTimedeltav2.delivery_time_gap(7, 3)
        self.assertEqual(result, 4)        

    def test_total_days(self):
        result = VKHWTestTimedeltav2.total_delivery_days(5, 2)
        self.assertEqual(result, 7)

    def test_faster_delivery(self):
        result = VKHWTestTimedeltav2.faster_delivery(4, 2)
        self.assertEqual(result, 2)


if __name__ == '__main__':
   unittest.main()

##############################################################
#Code Tested: VKHWTestTimedeltav2.py 
##############################################################
# I made two online purchases and expect deliveries from overstock.com and$
# Overstock delivery is set to arrive on 3/30/2020 and Nike on 3/23/2020.

#from datetime import date


#a = date(year=2020,month=3,day=30) #overstock item expected delivery

#b = date(year=2020,month=3,day=23) #nike item expected delivery

#def delivery_time_gap(a, b): #the number of days gap between the two deliveries
#    return a - b

#def total_delivery_days(a, b): #What's total number of days in transit for$
#    return a + b

#def faster_delivery(a, b):    #How many times is one delivery faster/slower     
#    return a / b 
#######################################################################
