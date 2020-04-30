import datetime
from datetime import date, timedelta
import unittest

class TestAdd(unittest.TestCase):
    """
    Test the add function from Python datetime library
    """

    def test_date_add_timedelta(self):
        """
        Test date add timedelta
        """
        random_date = datetime.datetime(2019,12,4,0,0)
        result = random_date + timedelta(days=30)
        self.assertEqual(result, datetime.datetime(2020,1,3,0,0))
        # self.assertEqual(result, date.fromisoformat('2020-01-03'))

    def test_date_substract_timedelta(self):
        """
        Test date substract timedelta
        """
        random_date = datetime.datetime(2020,1,2,0,0)
        result = random_date - timedelta(days=10)
        self.assertEqual(result, datetime.datetime(2019,12,23,0,0))
        # self.assertEqual(result, date.fromisoformat('2019-12-23'))

    def test_date_substract_date(self):
        """
        Test date substract date
        """
        random_date_1 = datetime.datetime(2020,1,2,0,0)
        random_date_2 = datetime.datetime(2019,10,2,0,0)
        result = random_date_1 - random_date_2
        self.assertEqual(result, datetime.timedelta(days=92))

    def test_timedelta_add_timedelta(self):
        """
        Test timedelta add timedelta
        """
        t1 = timedelta(seconds = 59)
        t2 = timedelta(minutes = 2, seconds = 30 )
        result = t1 + t2
        self.assertEqual(result, datetime.timedelta(seconds=209))

    def test_timedelta_substract_timedelta(self):
        """
        Test test timedelta substract timedelta
        """
        t1 = timedelta(days = 1, minutes = 1, seconds = 60)
        t2 = timedelta(seconds = 30)
        result = t1 - t2
        self.assertEqual(result, datetime.timedelta(days=1, seconds=90))


if __name__ == '__main__':
    unittest.main()
