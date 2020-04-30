# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 23:27:43 2020  @author: Mary Liu
Use unittest.TestCase methods to confirm that the addition 
and subtraction of date and timedelta objects produce correct results
"""

import unittest
from datetime import timedelta, date, datetime

class num_year():
    def add_year(x):
        today = date.today()
        year = today.year + x
        return year

    def subtract_year(age):
        today = date.today()
        year = today.year - age
        return year
    
    def add_days(day):
        current = datetime.now()
        later = current + timedelta(days=day)
        return later.year
    
    def subtract_days(day):
        current = datetime.now()
        past = current - timedelta(days=day)
        return past.year
    
class test_num_year(unittest.TestCase):
    def test_add_year(self):
        self.assertEqual(num_year.add_year(20),2040)
        
    def test_subtract_year(self):
        self.assertEqual(num_year.subtract_year(10),2010)
        
    def test_add_days(self):
        self.assertEqual(num_year.add_days(365),2021)
    
    def test_subtract_days(self):
        self.assertEqual(num_year.subtract_days(365), 2019)
        
unittest.main(verbosity=2)