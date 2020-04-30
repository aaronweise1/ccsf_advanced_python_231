# PROMPT: Use unittest.TestCase methods to confirm that the addition and 
# subtraction of date and timedelta objects produce correct results

# THOUGHT PROCESS: I thought during this global pandemic that something 
# useful might be to calculate when quarantine will be over if it ends
# X days from today. In this example, I compare adding 90 days from 
# today's date with both the custom mymath module and the built in 
# addition of the datetime objects. For the subtraction example, I 
# check both methods to show that they result in the same answer when
# subtracting 90 days from today's date. I only output the test results,
# following the example from the reading, showing that in both cases
# the results match.

# PEER REVIEW: This program assumes that the peer reviewer has mymath.py 
# saved in the folder from which they run the program, otherwise import 
# mymath won't work. Please make sure to have mymath.py saved in your 
# folder when you run the program (see this week's reading for the code) 

import mymath
import unittest
import datetime

class TestMath(unittest.TestCase):
    """
    Test the add and subtract functions from the mymath library
    """
    def test_add_days(self):
        """
        Test that the addition of two datetime objects returns the correct total
        """
        result = mymath.add(datetime.date.today(),datetime.timedelta(days=90))
        self.assertEqual(result, datetime.date.today()+datetime.timedelta(days=90))
    def test_subtract_days(self):
        """
        Test that the subtraction of two datetime objects returns the correct 
	result
        """
        result = mymath.subtract(datetime.date.today(),datetime.timedelta(days=90))
        self.assertEqual(result, datetime.date.today()-datetime.timedelta(days=90))

if __name__ == '__main__':
    unittest.main()
